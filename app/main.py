from fastapi import FastAPI
from utils.custom_open_api import custom_openapi
from fastapi.middleware.cors import CORSMiddleware
from database.database import db_manager
from routers import router
from config.config import config
import contextlib
from cache.cache import get_redis_client


@contextlib.asynccontextmanager
async def life_span(app:FastAPI):
    print("Application starting up")
    await db_manager.connect_to_db()
    get_redis_client()
    yield
    print("cleangin up engines")
    await db_manager.clean_up_engines()

app = FastAPI(
    title='Boiler plate',
    root_path=f'/api/{config.app_name.lower()}',
    lifespan=life_span
)

app.openapi = lambda:custom_openapi(app)
# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
