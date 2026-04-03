from email.policy import default
from fastapi import FastAPI
from contextlib import asynccontextmanager
from helpers.config import get_settings
from routes import base, data , nlp
from stores.llm.LLMProviderFactory import LLMProviderFactory
from stores.llm.templates.template_parser import TemplateParser
from stores.vectordb.VectorDBProviderFactory import VectorDBProviderFactory
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

#The method "on_event" in class "FastAPI" is deprecated
#on_event is deprecated, use lifespan event handlers instead.

@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    
    postgres_conn = f"postgresql+asyncpg://{settings.POSTGRESQL_USERNAME}:{settings.POSTGRESQL_PASSWORD}@{settings.POSTGRESQL_HOST}:{settings.POSTGRESQL_PORT}/{settings.POSTGRESQL_MAIN_DB}"

    app.db_engine = create_async_engine(postgres_conn)
    app.db_client = sessionmaker(
        app.db_engine, class_=AsyncSession, expire_on_commit=False
    )

    llm_provider_factory = LLMProviderFactory(settings)
    vectordb_provider_factory=VectorDBProviderFactory(settings)
    # generation client
    app.generation_client = llm_provider_factory.create(provider=settings.GENERATION_BACKEND)
    app.generation_client.set_generation_model(model_id = settings.GENERATION_MODEL_ID)

    # embedding client
    app.embedding_client = llm_provider_factory.create(provider=settings.EMBEDDING_BACKEND)
    app.embedding_client.set_embedding_model(model_id=settings.EMBEDDING_MODEL_ID,
                                             embedding_size=settings.EMBEDDING_MODEL_SIZE)
    
    #vector db client
    app.vectordb_client=vectordb_provider_factory.create(
        provider=settings.VECTOR_DB_BACKEND
    )
    app.vectordb_client.connect()

    app.template_parser = TemplateParser(
        language= settings.PRIMARY_LANG,
        default_language=settings.DEFAULT_LANG,
    )

    yield  # App is running

    app.db_engine.dispose()  # On shutdown
    app.vectordb_client.disconnect()

app = FastAPI(lifespan=lifespan)

# Register routers
app.include_router(base.base_router)
app.include_router(data.data_router)
app.include_router(nlp.nlp_router)