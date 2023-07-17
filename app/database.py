import os

from tortoise import Tortoise
from dotenv import load_dotenv

load_dotenv()

DB_IP = os.getenv('DB_IP')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

if not DB_IP or not DB_PORT or not DB_NAME or not DB_USER or not DB_PASS:
    raise Exception('Database credentials not found')


async def init_db():
    await Tortoise.init(
        db_url=f'postgres://{DB_USER}:{DB_PASS}@{DB_IP}:{DB_PORT}/{DB_NAME}',
        modules={'models': ['app.models']}
    )
    await Tortoise.generate_schemas()
    print('Database initialized')
