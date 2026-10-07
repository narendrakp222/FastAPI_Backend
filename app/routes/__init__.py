from app.routes.employee_route import router 
from fastapi import APIRouter

apirouter=APIRouter()

apirouter.include_router(router)