from fastapi import APIRouter

from app.models import CargoType, InsuranceRequest
import tortoise

router = APIRouter()


@router.get("/calculate-insurance")
async def calculate_insurance(declared_value: float, cargo_type: str, date: str):
    try:
        # Получение тарифа по типу груза и дате из БД получение всех значение по типу груза и дате
        tariff = await CargoType.get(name=cargo_type, date=date)
        print(tariff)
        rate = tariff.rate

        insurance_cost = declared_value * rate
        a = await InsuranceRequest.create(rate=rate,
                                          cargo_type_id=tariff.id)
        print('a:', a)
        return {"insurance_cost": insurance_cost}
    except tortoise.exceptions.DoesNotExist:
        return {"error": "Invalid cargo type or date"}
    # except Exception as e:
    #     return {"error": str(e)}
