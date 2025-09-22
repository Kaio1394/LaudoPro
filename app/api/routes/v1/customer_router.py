from fastapi import APIRouter

customer_router_v1 = APIRouter(prefix="/api/v1", tags=["Customer"])

@customer_router_v1.get("/customer")
async def get_customer():
    return {"message": "Bem-vindo ao meu projeto FastAPI 🚀"}

@customer_router_v1.post("/customer")
async def get_customer():
    return {"message": "Bem-vindo ao meu projeto FastAPI 🚀"}