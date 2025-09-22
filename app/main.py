from fastapi import FastAPI
from app.api.routes import customer_router

app = FastAPI(title="Meu Projeto FastAPI")
app.include_router(customer_router)