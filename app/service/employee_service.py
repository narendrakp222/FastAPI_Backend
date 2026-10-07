# # from app.model.employeemodel import Employee
# # from sqlalchemy.orm import Session


# # def getemployeeservice(db:Session):
# #     empoyee=db.query(Employee).all()
# #     return empoyee


# from app.model.employeemodel import users
# from sqlalchemy.orm import Session
# def service_user(db:Session):
#     employee=db.query(users).all()
#     return employee

from sqlalchemy.orm import Session
from app.model.employeemodel import user


def user_service(db:Session):
    users=db.query(user).all()
    return users