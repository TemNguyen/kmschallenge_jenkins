import motor.motor_asyncio
import certifi
import json
import os


# Load cluster url từ file json
with open(os.path.join(os.path.dirname(__file__), '../core/config.json'), "r") as file:
    config = json.load(file)

MONGODB_URL = config["cluster"]
DATABASE_NAME = config["database"]


class Database():
    def __init__(self) -> None:
        self.connected = False
        self.client = None

    async def db_connection(self):
        if self.connected == False:
            self.client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL, tlsCAFile=certifi.where())
            self.connected = True
        return self.client[DATABASE_NAME]