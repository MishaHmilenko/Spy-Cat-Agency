from src.business_logic.target.dto import CreateTargetDTO, BaseTargetDTO, UpdateTargetDTO
from src.business_logic.target.exceptions import TargetNotExist, TargetAlreadyComplete
from src.db.repositories.target import TargetRepository


class TargetBusinessLogicService:

    def __init__(self, target_repo: TargetRepository) -> None:
        self.target_repo = target_repo

    async def create_target(self, target_data: CreateTargetDTO) -> BaseTargetDTO:
        target = await self.target_repo.create(target_data)

        return BaseTargetDTO(
            id=target.id,
            name=target.name,
            country=target.country,
            notes=target.notes,
            complete=target.complete
        )

    async def update_target(self, target_id: int, target_data: UpdateTargetDTO) -> None:
        target_obj = await self.target_repo.get_by_id(target_id)

        if not target_obj:
            raise TargetNotExist()

        if target_obj.complete:
            raise TargetAlreadyComplete()

        await self.target_repo.update_target(target_id, target_data)

    async def get_target(self, target_id: int) -> BaseTargetDTO:
        target = await self.target_repo.get_by_id(target_id)

        if target is None:
            raise TargetNotExist()

        return BaseTargetDTO(
            id=target.id,
            name=target.name,
            country=target.country,
            notes=target.notes,
            complete=target.complete,
            mission_id=target.mission_id
        )

    async def get_all_targets(self) -> list[BaseTargetDTO]:
        targets = await self.target_repo.get_all()

        return [BaseTargetDTO(
            id=target.id,
            name=target.name,
            country=target.country,
            notes=target.notes,
            complete=target.complete,
            mission_id=target.mission_id
        ) for target in targets]

    async def is_target_complete(self, target_id: int) -> bool:
        target = await self.target_repo.get_by_id(target_id)

        if target is None:
            raise TargetNotExist()

        return target.complete

    async def delete_target(self, target_id: int) -> None:
        await self.target_repo.delete(target_id)

    async def get_all_targets_by_mission(self, mission_id: int) -> list[BaseTargetDTO]:
        targets = await self.target_repo.get_all_targets_by_mission_id(mission_id)

        return [BaseTargetDTO(
            id=target.id,
            name=target.name,
            country=target.country,
            notes=target.notes,
            complete=target.complete,
            mission_id=target.mission_id
        ) for target in targets]

    async def is_target_belongs_to_mission(self, target_id: int, mission_id: int) -> bool:

        if await self.target_repo.get_by_id(target_id) is None:
            raise TargetNotExist()

        target = await self.target_repo.get_by_id(target_id)

        return target.mission_id == mission_id
