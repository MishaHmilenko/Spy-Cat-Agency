from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter

from src.business_logic.target.dto import CreateTargetDTO, BaseTargetDTO, UpdateTargetDTO
from src.business_logic.target.logic import TargetBusinessLogicService

router = APIRouter(prefix='/target', tags=['Target'])


@router.post('/create')
@inject
async def create_target(
    target_data: CreateTargetDTO, service: FromDishka[TargetBusinessLogicService]
) -> BaseTargetDTO:
    return await service.create_target(target_data)


@router.delete('/delete/{target_id}')
@inject
async def delete_target(
    target_id: int, service: FromDishka[TargetBusinessLogicService]
) -> None:
    await service.delete_target(target_id)


@router.patch('/update/{target_id}')
@inject
async def update_target(
    target_id: int, target_data: UpdateTargetDTO, service: FromDishka[TargetBusinessLogicService]
) -> BaseTargetDTO:
    await service.update_target(target_id, target_data)
    return await service.get_target(target_id)


@router.get('/get/{target_id}')
@inject
async def get_target(
    target_id: int, service: FromDishka[TargetBusinessLogicService]
) -> BaseTargetDTO:
    return await service.get_target(target_id)


@router.get('/get-all')
@inject
async def get_all(
    service: FromDishka[TargetBusinessLogicService]
) -> list[BaseTargetDTO]:
    return await service.get_all_targets()
