from typing import Generic, TypeVar, Sequence

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models.base import Base

Model = TypeVar('Model', bound=Base)


class BaseRepository(Generic[Model]):
    def __init__(self, model, session: AsyncSession) -> None:
        self._model = model
        self._session = session

    async def get_by_id(self, id_: int) -> Model:
        query = select(self._model).where(self._model.id == id_)
        return (await self._session.execute(query)).scalar_one_or_none()

    async def get_all(self) -> Sequence[Model]:
        query = select(self._model)
        return (await self._session.execute(query)).scalars().all()

    async def delete(self, id_: int) -> None:
        query = delete(self._model).where(self._model.id == id_)
        await self._session.execute(query)
