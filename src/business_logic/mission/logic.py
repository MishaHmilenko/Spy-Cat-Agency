from src.business_logic.mission.dto import CreateMissionDTO, BaseMissionDTO, UpdateMissionDTO
from src.business_logic.mission.exceptions import MissionAlreadyAssignedError, MissionNotExist
from src.business_logic.spy_cat.exceptions import SpyCatNotFound
from src.business_logic.spy_cat.logic import SpyCatBusinessLogicService
from src.business_logic.target.dto import UpdateTargetDTO
from src.business_logic.target.exceptions import TargetNotExist, TargetNotBelongsToMission
from src.business_logic.target.logic import TargetBusinessLogicService
from src.db.repositories.mission import MissionRepository
from src.db.repositories.spy_cat import SpyCatRepository
from src.db.repositories.target import TargetRepository


class MissionBusinessLogicService:

    def __init__(
            self,
            mission_repo: MissionRepository,
            target_service: TargetBusinessLogicService,
            target_repo: TargetRepository,
            spy_cat_service: SpyCatBusinessLogicService,
            spy_cat_repo: SpyCatRepository
    ) -> None:
        self.mission_repo = mission_repo
        self.target_service = target_service
        self.target_repo = target_repo
        self.spy_cat_service = spy_cat_service
        self.spy_cat_repo = spy_cat_repo

    async def create_mission(self, data: CreateMissionDTO) -> BaseMissionDTO:
        targets_data = data.targets
        del data.targets

        mission = await self.mission_repo.create_mission(data)

        if targets_data:
            for target_data in targets_data:
                target_data.mission_id = mission.id
                await self.target_repo.create(target_data)

        return BaseMissionDTO(
            id=mission.id,
            name=mission.name,
            executor=await self.spy_cat_service.get_spy_cat(int(mission.executor)) if mission.executor else None,
            targets=await self.target_service.get_all_targets_by_mission(mission.id)
        )

    async def get_mission(self, mission_id: int) -> BaseMissionDTO:

        if await self.mission_repo.get_by_id(mission_id) is None:
            raise MissionNotExist()

        mission = await self.mission_repo.get_by_id(mission_id)

        return BaseMissionDTO(
            id=mission.id,
            name=mission.name,
            executor=await self.spy_cat_service.get_spy_cat(mission.executor_id) if mission.executor_id else None,
            targets=await self.target_service.get_all_targets_by_mission(mission.id)
        )

    async def get_all_missions(self) -> list[BaseMissionDTO]:
        missions = await self.mission_repo.get_all()

        return [BaseMissionDTO(
            id=mission.id,
            name=mission.name,
            executor=await self.spy_cat_service.get_spy_cat(int(mission.executor)) if mission.executor else None,
            targets=await self.target_service.get_all_targets_by_mission(mission.id)
        ) for mission in missions]

    async def update_mission(self, mission_id: int, data: UpdateMissionDTO) -> None:

        if await self.mission_repo.get_by_id(mission_id) is None:
            raise MissionNotExist()
        for target_data in data.targets:
            target_data_id = target_data.target_id
            del target_data.target_id

            if not await self.target_service.is_target_belongs_to_mission(target_data_id, mission_id):
                raise TargetNotBelongsToMission()

            await self.target_service.update_target(
                target_data_id, UpdateTargetDTO(**target_data.dict(exclude_unset=True))
            )

    async def is_mission_assigned_to_cat(self, mission_id: int) -> bool:

        if await self.mission_repo.get_by_id(mission_id) is None:
            raise MissionNotExist()

        mission = await self.mission_repo.get_by_id(mission_id)
        return mission.executor is None

    async def delete_mission(self, mission_id: int) -> None:

        if await self.mission_repo.get_by_id(mission_id) is None:
            raise MissionNotExist()

        if not await self.is_mission_assigned_to_cat(mission_id):
            raise MissionAlreadyAssignedError()

        await self.mission_repo.delete(mission_id)

    async def add_target_to_mission(self, target_id: int, mission_id: int) -> None:
        mission = await self.mission_repo.get_by_id(mission_id)
        target = await self.target_repo.get_by_id(target_id)

        if mission is None:
            raise MissionNotExist()

        if target is None:
            raise TargetNotExist()

        await self.target_repo.update_mission_id_field(target, mission.id)
        await self.mission_repo.add_record_to_targets(target, mission)

    async def add_executor_to_mission(self, executor_id: int, mission_id: int) -> None:
        mission = await self.mission_repo.get_by_id(mission_id)
        executor = await self.spy_cat_repo.get_by_id(executor_id)

        if mission is None:
            raise MissionNotExist()

        if executor is None:
            raise SpyCatNotFound()

        await self.mission_repo.add_record_to_executor(executor, mission)
