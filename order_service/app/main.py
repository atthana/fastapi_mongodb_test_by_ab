from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import db_manager
from app.routers import order_router

# ใช้ lifespan เพื่อจัดการเรื่องการเปิด/ปิดฐานข้อมูลเมื่อเซิร์ฟเวอร์เปิดหรือปิดตัวลง
@asynccontextmanager
async def lifespan(app: FastAPI):
    db_manager.connect() # เปิด Connection ตอนแอปเริ่มทำงาน
    yield
    db_manager.close()   # ปิด Connection ตอนแอปโดนสั่งปิด

app = FastAPI(title="Async Order Service", lifespan=lifespan)

# ลงทะเบียน Router
app.include_router(order_router.router)