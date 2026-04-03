from .redarag_base import SQLAlchemyBase
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Integer, String, Index, func
from sqlalchemy.dialects.postgresql import UUID , JSONB
from sqlalchemy.orm import relationship
from pydantic import BaseModel
import uuid

class DataChunk(SQLAlchemyBase):
    __tablename__ = "chunks"

    chunk_id = Column(Integer, primary_key=True, autoincrement=True)
    chunk_uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    chunk_text= Column(String, nullable=False)
    chunk_metadata = Column(JSONB, nullable=False)
    chunk_order = Column(Integer, nullable=False)

    chunk_asset_id = Column(Integer, ForeignKey("assets.asset_id"), nullable=False)  # Foreign key to Asset.asset_id
    asset=relationship("Asset", back_populates="chunks")  # Establish relationship with Asset

    chunk_project_id = Column(Integer, ForeignKey("projects.project_id"), nullable=False)  # Foreign key to Project.project_id
    project=relationship("Project", back_populates="chunks")  # Establish relationship with Project

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now(), nullable=False)

    __table_args__ = (
        Index("ix_chunk_project_id", chunk_project_id),
        Index("ix_chunk_asset_id", chunk_asset_id),
    )

class RetrievedDocument(BaseModel):
    text: str
    score: float