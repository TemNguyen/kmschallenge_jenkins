from helpers.PyObjectId import PyObjectId
from pydantic import BaseModel, Field
from typing import Optional, List
from bson import ObjectId

class User(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    fullname: str
    bibCode: str
    identityImages: List[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

class UserUpsert(BaseModel):
    username: str
    password: str
    fullname: str
    bibCode: str
