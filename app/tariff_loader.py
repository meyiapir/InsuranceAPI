import json

def load_tariff_from_file(filename):
    with open(filename, 'r') as file:
        tariff = json.load(file)
    return tariff


