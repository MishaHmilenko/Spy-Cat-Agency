from pydantic import BaseModel


class CreateSpyCatDTO(BaseModel):
    name: str
    years_of_experience: int
    breed: str
    salary: float


class UpdateSpyCatDTO(BaseModel):
    salary: float


class BaseSpyCatDTO(BaseModel):
    id: int
    name: str
    years_of_experience: int
    breed: str
    salary: float