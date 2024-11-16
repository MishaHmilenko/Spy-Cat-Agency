from src.business_logic.spy_cat.dto import CreateSpyCatDTO, BaseSpyCatDTO, UpdateSpyCatDTO
from src.business_logic.spy_cat.exceptions import ValidateBreedError, SpyCatNotFound
from src.business_logic.spy_cat.validator_api import CatBreedValidator
from src.db.repositories.spy_cat import SpyCatRepository


class SpyCatBusinessLogicService:

    def __init__(
            self, spy_cat_repo: SpyCatRepository, cat_validator: CatBreedValidator
    ) -> None:
        self.spy_cat_repo = spy_cat_repo
        self.cat_validator = cat_validator

    async def create_spy_cat(self, spy_cat_data: CreateSpyCatDTO) -> BaseSpyCatDTO:

        if not await self.cat_validator.validate_breed(spy_cat_data.breed):
            raise ValidateBreedError()

        spy_cat = await self.spy_cat_repo.create(spy_cat_data)

        return BaseSpyCatDTO(
            id=spy_cat.id,
            name=spy_cat.name,
            years_of_experience=spy_cat.years_of_experience,
            breed=spy_cat.breed,
            salary=spy_cat.salary
        )

    async def delete_spy_cat(self, spy_cat_id: int) -> None:

        if await self.spy_cat_repo.get_by_id(spy_cat_id) is None:
            raise SpyCatNotFound()

        await self.spy_cat_repo.delete(spy_cat_id)

    async def update_spy_cat(self, spy_cat_id: int, spy_cat_data: UpdateSpyCatDTO) -> None:

        if await self.spy_cat_repo.get_by_id(spy_cat_id) is None:
            raise SpyCatNotFound()

        await self.spy_cat_repo.update(spy_cat_id, spy_cat_data)

    async def get_spy_cat(self, spy_cat_id: int) -> BaseSpyCatDTO:

        if await self.spy_cat_repo.get_by_id(spy_cat_id) is None:
            raise SpyCatNotFound()

        spy_cat = await self.spy_cat_repo.get_by_id(spy_cat_id)

        return BaseSpyCatDTO(
            id=spy_cat.id,
            name=spy_cat.name,
            years_of_experience=spy_cat.years_of_experience,
            breed=spy_cat.breed,
            salary=spy_cat.salary
        )

    async def get_all_spy_cats(self) -> list[BaseSpyCatDTO]:
        spy_cats = await self.spy_cat_repo.get_all()

        return [BaseSpyCatDTO(
            id=spy_cat.id,
            name=spy_cat.name,
            years_of_experience=spy_cat.years_of_experience,
            breed=spy_cat.breed,
            salary=spy_cat.salary
        ) for spy_cat in spy_cats]
