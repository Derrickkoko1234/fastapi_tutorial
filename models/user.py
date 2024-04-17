# models/user.py
from pydantic import BaseModel
from typing import Optional
from bson import ObjectId


class User(BaseModel):
    _id: Optional[ObjectId]
    name: str
    email: str

    # class Config:
    #     arbitrary_types_allowed = True
