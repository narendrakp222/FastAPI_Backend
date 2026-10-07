# # from sqlalchemy.orm import Session

# # from app.service.employee_service import getemployeeservice

# # def employee_controller(db:Session):
# #     return getemployeeservice(db)

# from app.service.employee_service import service_user
# from sqlalchemy.orm import Session
# def user_controller(db:Session):
#     return service_user(db)

from sqlalchemy.orm import Session
from app.service.employee_service import user_service
def user_controller(db:Session):
    return user_service(db)