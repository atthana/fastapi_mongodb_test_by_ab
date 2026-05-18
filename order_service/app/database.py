from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

class MongoDB:
    def __init__(self):
        self.client = None
        self.db = None

    def connect(self):
        # maxPoolSize จำกัด Connection ไม่ให้ล้น, minPoolSize เปิดสแตนด์บายไว้ลด Latency
        self.client = AsyncIOMotorClient(
            settings.MONGO_URI, 
            maxPoolSize=50, 
            minPoolSize=10
        )
        self.db = self.client[settings.DB_NAME]
        print("Connected to MongoDB with Connection Pool!")

    def close(self):
        if self.client:
            self.client.close()
            print("MongoDB Connection Closed.")

db_manager = MongoDB()