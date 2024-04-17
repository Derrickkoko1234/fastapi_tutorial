# models/response.py
from pydantic import BaseModel
from typing import Optional, Generic, TypeVar, Any

T = TypeVar('T')

class ResponseModel(Generic[T], BaseModel):
    status: bool
    message: str
    data: Optional[T] = None
