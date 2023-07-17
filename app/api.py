import tortoise
from fastapi import APIRouter
from loguru import logger

from app.models import CargoType, InsuranceRequest

router = APIRouter()  # Создание экземпляра роутера


@router.get("/calculate_insurance")
async def calculate_insurance(declared_value: float, cargo_type: str, date: str):
    try:
        # Получение тарифа по типу груза и дате из БД
        tariff = await CargoType.get(name=cargo_type, date=date)
        rate = tariff.rate  # Получение ставки из тарифа

        insurance_cost = declared_value * rate  # Расчет стоимости страховки
        await InsuranceRequest.create(rate=rate,
                                      cargo_type_id=tariff.id)  # Сохранение запроса в БД
        return {"insurance_cost": insurance_cost}
    except tortoise.exceptions.DoesNotExist:
        return {"error": "Invalid cargo type or date"}

    except Exception as e:
        logger.error(f"Error calculating insurance: {e}")
        return {"error": str(e)}


@router.post("/add_tariff")
async def add_tariff(cargo_type: str, rate: float, date: str):
    try:
        await CargoType.create(name=cargo_type, rate=rate, date=date)  # Сохранение тарифа в БД
        return {"status": "ok"}
    except Exception as e:
        logger.error(f"Error adding tariff: {e}")
        return {"error": str(e)}
