import json

def load_tariff_from_file(filename):
    with open(filename, 'r') as file:
        tariff = json.load(file)
    return tariff

# Загрузка тарифа через API
# def load_tariff_from_api():
#     # ваш код для загрузки тарифа из API
#     pass
