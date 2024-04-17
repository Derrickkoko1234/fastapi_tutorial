# views/user.py
from fastapi import APIRouter, HTTPException
from bson import ObjectId
from db import Database
from models.user import User
from models.response import ResponseModel

router = APIRouter()


@router.post("/user", response_model=ResponseModel[User])
async def create_user(user: User):
    users_collection = Database.db.users
    result = users_collection.insert_one(
        user.dict()
    )  # Exclude 'id' as it is None initially
    if result.inserted_id:
        user._id = result.inserted_id
        return ResponseModel[User](
            status=True, message="User created successfully", data={"user": user}
        )
    raise HTTPException(status_code=500, detail="Failed to create user")


@router.get("/user/{user_id}", response_model=ResponseModel[User])
async def get_user(user_id: str):
    users_collection = Database.db.users
    user_data = users_collection.find_one({"_id": ObjectId(user_id)})
    if user_data:
        user = User(**user_data)
        return ResponseModel[User](
            status=True, message="User retrieved successfully", data={"user": user}
        )
    return ResponseModel[User](status=False, message="User not found", data=None)
