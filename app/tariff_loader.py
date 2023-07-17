import json

from loguru import logger

from app.models import CargoType


async def load_tariff_to_db(filename):
    with open(filename, 'r') as file:
        tariff = json.load(file)

    for date, tariff_data_list in tariff.items():
        for tariff_data in tariff_data_list:
            cargo_type = tariff_data['cargo_type']
            rate = tariff_data['rate']
            try:
                await CargoType.get_or_create(name=cargo_type, rate=rate, date=date)
            except Exception as e:
                logger.error(f"Error creating tariff: {e}")
