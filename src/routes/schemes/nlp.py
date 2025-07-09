from typing import Optional
from pydantic import BaseModel

class PushRequest(BaseModel):
    
    do_reset : Optional[int] = 0
