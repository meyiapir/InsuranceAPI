import tortoise
from fastapi import APIRouter
from loguru import logger

from app.models import CargoType, InsuranceRequest

router = APIRouter()


@router.get("/calculate-insurance")
async def calculate_insurance(declared_value: float, cargo_type: str, date: str):
    try:
        # Получение тарифа по типу груза и дате из БД получение всех значение по типу груза и дате
        tariff = await CargoType.get(name=cargo_type, date=date)
        rate = tariff.rate

        insurance_cost = declared_value * rate
        await InsuranceRequest.create(rate=rate,
                                      cargo_type_id=tariff.id)
        return {"insurance_cost": insurance_cost}
    except tortoise.exceptions.DoesNotExist:
        return {"error": "Invalid cargo type or date"}

    except Exception as e:
        logger.error(f"Error calculating insurance: {e}")
        return {"error": str(e)}
