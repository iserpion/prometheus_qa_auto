from pydantic import BaseModel, Field
from modules.common.data.enums import PetStatus


class PetCategory(BaseModel):
    id: int
    name: str


class PetTag(BaseModel):
    id: int
    name: str


class Pet(BaseModel):
    id: int
    category: PetCategory
    name: str
    photo_urls: list[str] = Field(alias="photoUrls")
    tags:  list[PetTag]
    status: PetStatus
