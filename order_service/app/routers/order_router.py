from fastapi import APIRouter, HTTPException
from app.models.order_model import OrderCreateInput
from app.database import db_manager
from datetime import datetime

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/")
async def create_order(payload: OrderCreateInput):
    # 1. แปลงข้อมูลจาก Pydantic เป็น Dictionary เพื่อเซฟลง Mongo
    order_dict = payload.model_dump()
    order_dict["status"] = "PENDING"
    order_dict["created_at"] = datetime.utcnow()
    
    # 2. เรียกใช้ collection (เหมือนระบุตารางใน SQL)
    collection = db_manager.db["orders"]
    
    # 3. บันทึกข้อมูลแบบ Async (ใช้ await เพื่อไม่ให้ block thread)
    result = await collection.insert_one(order_dict)
    
    return {"status": "success", "order_id": str(result.inserted_id)}

@router.get("/{customer_id}")
async def get_orders(customer_id: str):
    collection = db_manager.db["orders"]
    orders = []
    
    # .find() จะส่งค่าคืนมาเป็น Cursor เราต้องใช้ async for ในการดึงข้อมูลออกมาแบบดึงทีละตัวไม่ block
    cursor = collection.find({"customer_id": customer_id})
    async for document in cursor:
        document["_id"] = str(document["_id"]) # แปลง ObjectId เป็น String เพื่อพ่นเป็น JSON
        orders.append(document)
        
    if not orders:
        raise HTTPException(status_code=404, detail="No orders found")
        
    return {"customer_id": customer_id, "orders": orders}