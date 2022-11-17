from helpers.PyObjectId import PyObjectId
from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class Auth(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    username: str
    password: str
    userId: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

class LoginModel(BaseModel):
    username: str
    password: str
