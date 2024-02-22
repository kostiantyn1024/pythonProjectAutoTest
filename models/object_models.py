from typing import List

from pydantic import BaseModel, Field


class ObjectData(BaseModel):
    generation: str = Field(alias="Generation")
    price: str = Field(alias="Price")
    capacity: str = Field(alias="Capacity")


class CustomObj(BaseModel):
    name: str


class CustomObjData(BaseModel):
    bool: bool
    int: int
    float: float
    string: str
    array: List[str]
    obj: CustomObj


class ObjectOutSchema(BaseModel):
    id: str
    name: str
    data: ObjectData


class ObjectCreateOutSchema(BaseModel):
    id: str
    name: str | None
    data: ObjectData | None
    createdAt: str


class CustomObjCreateOutSchema(BaseModel):
    id: str
    name: str
    data: CustomObjData
    createdAt: str


class ObjectUpdateOutSchema(BaseModel):
    id: str
    name: str | None
    data: ObjectData | None
    updatedAt: str


class CustomObjUpdateOutSchema(BaseModel):
    id: str
    name: str
    data: CustomObjData
    updatedAt: str
