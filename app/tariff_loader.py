import json

from app.models import CargoType


async def load_tariff_to_db(filename):
    with open(filename, 'r') as file:
        tariff = json.load(file)

    for date_type in tariff.items():
        for tariff_data in date_type[1]:
            cargo_type = tariff_data['cargo_type']
            rate = tariff_data['rate']
            await CargoType.get_or_create(name=cargo_type, rate=rate, date=date_type[0])


