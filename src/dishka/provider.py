from dishka import Provider, provide, Scope
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncEngine, AsyncSession

from src.business_logic.mission.logic import MissionBusinessLogicService
from src.business_logic.spy_cat.logic import SpyCatBusinessLogicService
from src.business_logic.spy_cat.validator_api import CatBreedValidator
from src.business_logic.target.logic import TargetBusinessLogicService
from src.db.main import DBConfig
from src.db.models.mission import Mission
from src.db.models.spy_cat import SpyCat
from src.db.models.target import Target
from src.db.repositories.mission import MissionRepository
from src.db.repositories.spy_cat import SpyCatRepository
from src.db.repositories.target import TargetRepository


class DishkaProvider(Provider):

    @provide(scope=Scope.APP)
    async def get_engine(self) -> AsyncEngine:
        return create_async_engine(url=DBConfig().url)

    @provide(scope=Scope.APP)
    async def get_db_config(self, engine: AsyncEngine) -> AsyncSession:
        async_session = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
        return async_session()

    @provide(scope=Scope.APP)
    async def get_spy_cat_validator(self) -> CatBreedValidator:
        return CatBreedValidator()

    @provide(scope=Scope.APP)
    async def get_spy_cat_repo(self, session: AsyncSession) -> SpyCatRepository:
        return SpyCatRepository(session=session)

    @provide(scope=Scope.APP)
    async def get_target_repo(self, session: AsyncSession) -> TargetRepository:
        return TargetRepository(session=session)

    @provide(scope=Scope.APP)
    async def get_mission_repo(self, session: AsyncSession) -> MissionRepository:
        return MissionRepository(session=session)

    @provide(scope=Scope.APP)
    async def get_spy_cat_service(
            self, spy_cat_repo: SpyCatRepository, cat_validator: CatBreedValidator
    ) -> SpyCatBusinessLogicService:
        return SpyCatBusinessLogicService(spy_cat_repo=spy_cat_repo, cat_validator=cat_validator)

    @provide(scope=Scope.APP)
    async def get_target_service(self, target_repo: TargetRepository) -> TargetBusinessLogicService:
        return TargetBusinessLogicService(target_repo=target_repo)

    @provide(scope=Scope.APP)
    async def get_mission_service(
            self,
            mission_repo: MissionRepository,
            target_service: TargetBusinessLogicService,
            target_repo: TargetRepository,
            spy_cat_service: SpyCatBusinessLogicService,
            spy_cat_repo: SpyCatRepository
    ) -> MissionBusinessLogicService:

        return MissionBusinessLogicService(
            mission_repo=mission_repo,
            target_service=target_service,
            target_repo=target_repo,
            spy_cat_service=spy_cat_service,
            spy_cat_repo=spy_cat_repo
        )


provider = DishkaProvider()
