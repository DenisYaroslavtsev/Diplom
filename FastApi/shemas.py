from pydantic import BaseModel
from datetime import date


# from typing import Optional, List
# from fastapi import Body
# import json

class CreateUser(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    username: str
    email: str
    password: str
    repeat_password: str
    birth_date: date

# class DataModelOut(BaseModel):
#     message: str = None
#     id: str = None
#     input_data: dict = None
#     result: List[dict] = []
#     statusCode: int
#
#
# class DataModelIn(BaseModel):
#     countryId: str
#     policyDetails: List[dict]
#     leaveTypeId: str
#     branchIds: List[str]
#     cityIds: List[str]
#
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate_to_json
#
#     @classmethod
#     def validate_to_json(cls, value):
#         if isinstance(value, str):
#             return cls(**json.loads(value))
#         return value
#
#
# @router.post('/', response_model=DataModelOut)
# def create_policy_details(data: DataModelIn = Body(...), files: Optional[List[UploadFile]] = File(None)):
#     print('Files received: ', [f.filename for f in files])
#     return {'input_data': data, 'statusCode': status.HTTP_201_CREATED}
