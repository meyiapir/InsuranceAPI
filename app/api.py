from fastapi import APIRouter
from app.models import CargoType, InsuranceRequest
from app.tariff_loader import load_tariff_from_file
from app.database import init_db

router = APIRouter()


@router.get("/calculate-insurance")
async def calculate_insurance(declared_value: float, cargo_type: str):
    await init_db()
    tariff = load_tariff_from_file('tariff.json')
    cargo = await CargoType.get(name=cargo_type)
    rate = tariff.get(cargo.name)
    if rate is None:
        return {"error": "Invalid cargo type"}
    insurance_cost = declared_value * rate
    insurance_request = await InsuranceRequest.create(
        declared_value=declared_value,
        cargo_type=cargo
    )
    return {"insurance_cost": insurance_cost, "insurance_request_id": insurance_request.id}
