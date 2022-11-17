from helpers.ResponseModel import ResponseModel
from models.user import User
from models.auth import Auth, LoginModel
from services.srv_auth import (authenticate)
from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Auth"],
    responses={404: {"description": "Not found"}},
)

@router.post("/login")
async def login(account: LoginModel):
    user = await authenticate(account.username, account.password)

    if user:
        return ResponseModel(user, 200, "Login successfully.", False)
    else:
        return ResponseModel(user, 200, "Login failure, please check your account information!", True)
