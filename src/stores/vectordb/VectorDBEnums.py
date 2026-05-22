from enum import Enum

class VectorDBEnums(Enum):
    QDRANT = "QDRANT"
    PGVECTOR= "PGVECTOR"

class DistanceMethodEnums(Enum):
    COSINE = "cosine"
    DOT = "dot"

class PgVectorTableSchemeEnums(Enum):
    ID = "id"
    TEXT = "text" # optional, can be used to store the original text or a reference to it
    VECTOR = "vector"
    CHUNKID = "chunk_id"
    METADATA = "metadata"
    _PREFIX = "pgvector"

class PgVectorDistanceMethodEnums(Enum):
    COSINE = "vector_cosine_ops"
    DOT = "vector_l2_ops"

class PgVectorIndexTypeEnums(Enum):
    IVFFLAT = "IVFFLAT" # Default, greedy.
    HNSW = "HNSW" # Hierarchical Navigable Small World graphs