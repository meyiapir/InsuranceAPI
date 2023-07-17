# Insurance API

**- Тестовое задание для SMIT.Studio**

## Инструкция по запуску

### Без Docker

1. Склонировать репозиторий
2. Установить зависимости `pip install -r requirements.txt`
3. Создать файл `.env` в корне проекта и заполнить его данными для подключения к БД
4. Запустить БД через docker-compose `docker-compose up -d db`
5. Запустить приложение `python main.py`

### С Docker

1. Склонировать репозиторий
2. Создать файл `.env` в корне проекта и заполнить его данными для подключения к БД
3. Запустить приложение `docker-compose up -d`

## Документация

`/calculate_insurance` - `GET` 
- `declared_value` - Объявленная стоимость - `int`
- `cargo_type` - Тип груза - `str`
- `date` - Дата отправления - `str(YYYY-MM-DD)`

`/add_tariff` - `POST`
- `cargo_type` - Тип груза - `str`
- `rate` - Ставка - `int`
- `date` - Дата начала действия тарифа - `str(YYYY-MM-DD)`

## Используемые технологии
- **FastAPI**
- **PostgreSQL**
- **Docker**
- **Docker-compose**
- **Tortoise ORM**
- **Python 3.9**
