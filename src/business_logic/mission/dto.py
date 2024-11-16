from pydantic import BaseModel

from src.business_logic.spy_cat.dto import BaseSpyCatDTO
from src.business_logic.target.dto import BaseTargetDTO, CreateTargetDTO, UpdateMissionTargetsDTO, UpdateTargetDTO


class CreateMissionDTO(BaseModel):
    name: str
    targets: list[CreateTargetDTO] = []


class UpdateMissionDTO(BaseModel):
    targets: list[UpdateMissionTargetsDTO]


class BaseMissionDTO(BaseModel):
    id: int
    name: str
    executor: BaseSpyCatDTO | None
    targets: list[BaseTargetDTO] = []
