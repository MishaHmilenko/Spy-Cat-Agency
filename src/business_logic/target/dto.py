from pydantic import BaseModel


class CreateTargetDTO(BaseModel):
    name: str
    country: str
    notes: str
    mission_id: int | None = None


class UpdateTargetDTO(BaseModel):
    notes: str | None = None
    complete: bool | None = None


class UpdateMissionTargetsDTO(UpdateTargetDTO):
    target_id: int


class BaseTargetDTO(BaseModel):
    id: int
    name: str
    country: str
    notes: str | None
    complete: bool
    mission_id: int | None
