from helpers.CryptContext import verify_data
from db.driver import Database
from models.user import User

db = Database()

async def get_user(userId: str) -> User:
    try:
        cursor = await db.db_connection()
        user = await cursor.Users.find_one({"_id": userId})

        if user:
            return User(**user)
        else:
            return None
    except:
        return None

async def authenticate(username: str, password: str) -> User:
    try:
        cursor = await db.db_connection()
        user_auth = await cursor.Auth.find_one({"username": username})
        if user_auth and verify_data(password, user_auth['password']):         
            user = await get_user(user_auth['userId'])
            return user
        else:
            return None
    except:
        return None