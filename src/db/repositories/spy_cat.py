from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from src.business_logic.spy_cat.dto import CreateSpyCatDTO, UpdateSpyCatDTO
from src.db.models.spy_cat import SpyCat
from src.db.repositories.base import BaseRepository


class SpyCatRepository(BaseRepository):

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(model=SpyCat, session=session)

    async def create(self, data: CreateSpyCatDTO) -> SpyCat:
        obj = self._model(**data.dict())
        self._session.add(obj)
        await self._session.commit()
        await self._session.refresh(obj)
        return obj

    async def update(self, spy_cat_id: int, data: UpdateSpyCatDTO) -> None:
        query = update(self._model).where(self._model.id == spy_cat_id).values(**data.dict())
        await self._session.execute(query)
