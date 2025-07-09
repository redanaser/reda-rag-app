from fastapi import FastAPI, APIRouter, Request, status
from fastapi.responses import JSONResponse
from .schemes.nlp import PushRequest
from models.ProjectModel import ProjectModel
import logging

logger = logging.getLogger('uvicorn.error')

nlp_router = APIRouter(
    prefix='/api/v1/nlp',
    tags=["api_v1","nlp"]
)

@nlp_router.post("/index/push/{project_id}")
async def index_project(request : Request, project_id: str ,push_request: PushRequest ):
            
    project_model = await ProjectModel.create_instance(
        db_client=request.app.db_client
        )

    project = await project_model.get_project_or_create_one(
        project_id=project_id
        )
          