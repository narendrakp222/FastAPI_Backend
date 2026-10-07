# # from app.db.session import Base
# # from sqlalchemy import Column,Integer,String

# # class Employee(Base):
# #     __table__="employee"
# #     id=Column(Integer,primary_key=True)
# #     name=Column(String(50),nullable=False)
# #     email=Column(String(50),nullable=False)
# #     department=Column(String(50),nullable=False)
# #     salary=Column(String(50),nullable=False)


# from sqlalchemy import Column,Integer,String
# from app.db.session import Base 

# class users(Base):
#     __table__="users"
#     id=Column(Integer,primary_key=True)
#     name=Column(String(60),nullable=False)
#     email=Column(String(50),unique=True)
#     roll=Column(String(50),nullable=False)
#     age=Column(Integer,nullable=False)



from app.db.session import Base
from sqlalchemy import Column,Integer,String

class user(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    name=Column(String(50),nullable=False)
    age=Column(Integer,nullable=False)
    email=Column(String(60),unique=False)