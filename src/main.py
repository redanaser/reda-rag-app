from fastapi import FastAPI
from routes import base, data
from controllers import ProjectController

app =FastAPI()
app.include_router(base.base_router)
app.include_router(data.data_router)
