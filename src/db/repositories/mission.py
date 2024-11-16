from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from src.business_logic.mission.dto import CreateMissionDTO, UpdateMissionDTO
from src.db.models.mission import Mission
from src.db.models.spy_cat import SpyCat
from src.db.models.target import Target
from src.db.repositories.base import BaseRepository


class MissionRepository(BaseRepository):

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(model=Mission, session=session)

    async def create_mission(self, data: CreateMissionDTO) -> Mission:
        obj = self._model(**data.dict())
        self._session.add(obj)
        await self._session.commit()
        await self._session.refresh(obj)
        return obj

    async def add_record_to_targets(self, target: Target, mission: Mission) -> None:
        mission.targets.append(target)
        self._session.add(mission)
        await self._session.commit()

    async def add_record_to_executor(self, executor: SpyCat, mission: Mission) -> None:
        mission.executor_id = executor.id
        mission.executor = executor
        self._session.add(mission)
        await self._session.commit()

    async def update(self, _id: int, data: UpdateMissionDTO) -> None:
        query = update(self._model).where(self._model.id == _id).values(**data.dict())

        await self._session.execute(query)
