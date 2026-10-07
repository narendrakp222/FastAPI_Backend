# # from fastapi import APIRouter
# # from sqlalchemy.orm import Session
# # from app.db.session import get_db
# # from fastapi import Depends
# # from app.controller.employee_controller import employee_controller
# # from app.schemas.employee_schema import EmployeeResponse

# # router=APIRouter()

# # @router.get("/",response_model=list[EmployeeResponse])
# # def getemployee(db:Session=Depends(get_db)):
# #     return employee_controller


# from fastapi import APIRouter
# from sqlalchemy.orm import Session
# from app.db.session import get_db
# from fastapi import Depends

# router=APIRouter()

# @router.get("/users")
# def get_users(db:Session=Depends(get_db)):
#     return 

from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.controller.employee_controller import user_controller

router=APIRouter()
@router.get("/")
def getusers(db:Session=Depends(get_db)):
    return user_controller(db)









