from tortoise import Tortoise

DB_IP = 'localhost'
DB_PORT = '5432'
DB_NAME = 'insurancedb'
DB_USER = 'api_user'
DB_PASS = 'De1tY0urM0m'

async def init_db():
    await Tortoise.init(
        db_url=f'postgres://{DB_USER}:{DB_PASS}@{DB_IP}:{DB_PORT}/{DB_NAME}',
        modules={'models': ['app.models']}
    )
    await Tortoise.generate_schemas()
