from pydantic import BaseModel 
from typing import Optional 
from datetime import datetime 
 
class ItemCreate(BaseModel): 
    title: str 
    description: Optional[str] = None 
    status: Optional[str] = "new" 
 
class ItemUpdate(BaseModel): 
    title: Optional[str] = None 
    description: Optional[str] = None 
    status: Optional[str] = None 
 
class ItemResponse(BaseModel): 
    id: int 
    title: str 
    description: Optional[str] = None 
    status: str 
    created_at: datetime 
    updated_at: Optional[datetime] = None 
 
    class Config: 
        from_attributes = True 
