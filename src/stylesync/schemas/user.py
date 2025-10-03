from typing import Optional
from pydantic import BaseModel
from bson import ObjectId
from pydantic import Field, ConfigDict


class LoginPayload(BaseModel):
    username: str
    password: str


class UserCreate(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id")
    username: str
    password: str

    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True)


class UserResponse(BaseModel):
    id: str = Field(..., alias="id")
    username: str
