from typing import Sequence

from sqlalchemy import update, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.business_logic.target.dto import CreateTargetDTO, UpdateTargetDTO
from src.db.models.target import Target
from src.db.repositories.base import BaseRepository


class TargetRepository(BaseRepository):

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(model=Target, session=session)

    async def create(self, data: CreateTargetDTO) -> Target:
        obj = self._model(**data.dict())
        self._session.add(obj)
        await self._session.commit()
        await self._session.refresh(obj)
        return obj

    async def update_target(self, target_id: int, data: UpdateTargetDTO) -> None:
        query = update(self._model).where(self._model.id == target_id).values(**data.dict(exclude_unset=True))
        await self._session.execute(query)

    async def get_all_targets_by_mission_id(self, mission_id: int) -> Sequence[Target]:
        query = select(self._model).where(self._model.mission_id == mission_id)
        return (await self._session.execute(query)).scalars().all()

    async def update_mission_id_field(self, target: Target, mission_id: int) -> None:
        query = update(self._model).where(self._model.id == target.id).values(mission_id=mission_id)
        await self._session.execute(query)
