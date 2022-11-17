from helpers.ResponseModel import ResponseModel
from models.user import UserUpsert, User
from services.srv_user import create_user
from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/user",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def create(user: UserUpsert):
    try:
        new_user = await create_user(user)

        if new_user:
            return ResponseModel(new_user, 200, "User create successfully", False)
        else:
            return ResponseModel(new_user, 200, f"{user.username} is existed.", True)
    except Exception as e:
        return ResponseModel(None, 200, e, True)