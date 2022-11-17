from models.user import User, UserUpsert
from db.driver import Database
from helpers.PyObjectId import PyObjectId
from helpers.CryptContext import hash_data
from typing import List

db = Database()

async def read_user_by_id(userId: str) -> User:
    try:
        cursor = await db.db_connection()
        user = await cursor.Users.find({"_id": PyObjectId(userId)})
        
        if user:
            return User(**user)
        else:
            return None
    except:
        return None

async def create_user(newUser: UserUpsert) -> User:
    try:
        cursor = await db.db_connection()
        existedUser = await cursor.Auth.find_one({"username": newUser.username})

        if existedUser:
            return None
        else:
            hashedPassword = hash_data(newUser.password)
            user = await cursor.Users.insert_one({
                "fullname": newUser.fullname,
                "bibCode": newUser.bibCode,
                "identityImages": []
            })

            auth = await cursor.Auth.insert_one({
                "username": newUser.username,
                "password": hashedPassword,
                "userId": user.inserted_id
            })

            result = await cursor.Users.find_one({"_id": user.inserted_id})
            return User(**result)
    except:
        return None

# upload image to google drive
async def upload_user_image(userId: str, images: List[str]):
    pass

