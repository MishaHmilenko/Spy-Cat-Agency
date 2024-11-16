from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter

from src.business_logic.spy_cat.dto import CreateSpyCatDTO, UpdateSpyCatDTO, BaseSpyCatDTO
from src.business_logic.spy_cat.logic import SpyCatBusinessLogicService

router = APIRouter(prefix='/spy-cat', tags=['Spy Cat'])


@router.post('/create')
@inject
async def create_spy_cat(
        spy_cat_data: CreateSpyCatDTO, service: FromDishka[SpyCatBusinessLogicService]
) -> BaseSpyCatDTO:
    return await service.create_spy_cat(spy_cat_data)


@router.delete('/delete/{spy_cat_id}')
@inject
async def delete_spy_cat(
        spy_cat_id: int, service: FromDishka[SpyCatBusinessLogicService]
) -> None:
    await service.delete_spy_cat(spy_cat_id)


@router.patch('/update/{spy_cat_id}')
@inject
async def update_spy_cat(
        spy_cat_id: int, spy_cat_data: UpdateSpyCatDTO, service: FromDishka[SpyCatBusinessLogicService]
) -> BaseSpyCatDTO:
    await service.update_spy_cat(spy_cat_id, spy_cat_data)
    return await service.get_spy_cat(spy_cat_id)


@router.get('/get/{spy_cat_id}')
@inject
async def get_spy_cat(
        spy_cat_id: int, service: FromDishka[SpyCatBusinessLogicService]
) -> BaseSpyCatDTO:
    return await service.get_spy_cat(spy_cat_id)


@router.get('/get-all')
@inject
async def get_all_spy_cats(
        service: FromDishka[SpyCatBusinessLogicService]
) -> list[BaseSpyCatDTO]:
    return await service.get_all_spy_cats()
