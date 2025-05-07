from fastapi import FastAPI
from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings
from routes import base, data


#The method "on_event" in class "FastAPI" is deprecated
#on_event is deprecated, use lifespan event handlers instead.

@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)
    app.mongo_conn = mongo_conn
    app.db_client = mongo_conn[settings.MONGODB_DATABASE]
    
    yield  # App is running

    mongo_conn.close()  # On shutdown


app = FastAPI(lifespan=lifespan)

# Register routers
app.include_router(base.base_router)
app.include_router(data.data_router)
