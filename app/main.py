from fastapi import FastAPI
from app.api.routes.v1 import customer_router_v1

app = FastAPI(title="Laudo Pro")
app.include_router(customer_router_v1)