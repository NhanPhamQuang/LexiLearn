from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
db = client.lexilearn

user_collection = db.users
