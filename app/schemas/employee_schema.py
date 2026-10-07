# from pydantic import BaseModel,Field,EmailStr

# class EmployeeRequest(BaseModel):
#     name:str=Field(...,min_length=3,max_length=50)
#     email:EmailStr
#     department:str=Field(...,min_length=3)
#     salary:float | int = Field(gt=0)
# class EmployeeResponse(BaseModel):
#     id:int
#     name:str
#     email:str

from pydantic import BaseModel,Field,EmailStr

class RequestModel(BaseModel):
    id:int = Field(gt=0)
    name:str=Field(min_length=3,max_length=50)
    age:int=Field(gt=0)
    email:EmailStr

class ResponseModel(BaseModel):
    name:str
    age:int
    email:str

