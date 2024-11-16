from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter

from src.business_logic.mission.dto import CreateMissionDTO, BaseMissionDTO, UpdateMissionDTO
from src.business_logic.mission.logic import MissionBusinessLogicService
from src.business_logic.target.dto import UpdateMissionTargetsDTO

router = APIRouter(prefix='/mission', tags=['Mission'])


@router.post('/create')
@inject
async def create_mission(
    mission_data: CreateMissionDTO, service: FromDishka[MissionBusinessLogicService]
) -> BaseMissionDTO:
    return await service.create_mission(mission_data)


@router.post('/add-target/{target_id}/to-mission/{mission_id}')
@inject
async def add_target_to_mission(
    target_id: int, mission_id: int, service: FromDishka[MissionBusinessLogicService]
) -> BaseMissionDTO:
    await service.add_target_to_mission(target_id, mission_id)
    return await service.get_mission(mission_id)


@router.post('/add-executor/{executor_id}/to-mission/{mission_id}')
@inject
async def add_executor_to_mission(
    executor_id: int, mission_id: int, service: FromDishka[MissionBusinessLogicService]
) -> BaseMissionDTO:
    await service.add_executor_to_mission(executor_id, mission_id)
    return await service.get_mission(mission_id)


@router.delete('/delete/{mission_id}')
@inject
async def delete_mission(
        mission_id: int, service: FromDishka[MissionBusinessLogicService]
) -> None:
    await service.delete_mission(mission_id)


@router.patch('/update/{mission_id}')
@inject
async def update_mission(
        mission_id: int, mission_data: UpdateMissionDTO, service: FromDishka[MissionBusinessLogicService]
) -> BaseMissionDTO:
    await service.update_mission(mission_id, mission_data)
    return await service.get_mission(mission_id)


@router.get('/get/{mission_id}')
@inject
async def get_mission(
        mission_id: int, service: FromDishka[MissionBusinessLogicService]
) -> BaseMissionDTO:
    return await service.get_mission(mission_id)


@router.get('/get-all')
@inject
async def get_all_missions(
        service: FromDishka[MissionBusinessLogicService]
) -> list[BaseMissionDTO]:
    return await service.get_all_missions()
