from fastapi import APIRouter

customer_router = APIRouter()

@customer_router.get("api/customer/")
def get_customer():
    return {"message": "Bem-vindo ao meu projeto FastAPI 🚀"}

@customer_router.post("api/customer/")
def get_customer():
    return {"message": "Bem-vindo ao meu projeto FastAPI 🚀"}