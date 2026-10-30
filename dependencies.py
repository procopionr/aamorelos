from database.database import get_db
from fastapi import Depends
from repositories.area_repository import AreaRepository
from repositories.country_repository import CountryRepository
from repositories.district_repository import DistrictRepository
from repositories.evento_repository import EventoRepository
from repositories.group_gender_repository import GroupGenderRepository
from repositories.group_repository import GroupRepository
from repositories.group_type_repository import GroupTypeRepository
from repositories.language_repository import LanguageRepository
from repositories.municipality_repository import MunicipalityRepository
from repositories.reflexion_repository import ReflexionRepository
from repositories.region_repository import RegionRepository
from repositories.state_repository import StateRepository
from services.area_by_state_service import AreaByStateService
from services.area_service import AreaService
from services.country_service import CountryService
from services.district_by_state_service import DistrictByStateService
from services.district_service import DistrictService
from services.evento_service import EventoService
from services.group_by_district_service import GroupByDistrictService
from services.group_by_state_service import GroupByStateService
from services.group_gender_service import GroupGenderService
from services.group_service import GroupService
from services.group_type_service import GroupTypeService
from services.language_service import LanguageService
from services.reflexion_service import ReflexionService
from services.region_service import RegionService
from services.state_service import StateService
from sqlalchemy.orm import Session


def get_country_service(db: Session = Depends(get_db)) -> CountryService:
    return CountryService(CountryRepository(db))


def get_region_service(db: Session = Depends(get_db)) -> RegionService:
    return RegionService(RegionRepository(db))


def get_area_service(db: Session = Depends(get_db)) -> AreaService:
    return AreaService(AreaRepository(db), RegionRepository(db))


def get_area_by_state_service(db: Session = Depends(get_db)) -> AreaByStateService:
    return AreaByStateService(AreaRepository(db), MunicipalityRepository(db), StateRepository(db))


def get_state_service(db: Session = Depends(get_db)) -> StateService:
    return StateService(StateRepository(db))


def get_district_service(db: Session = Depends(get_db)) -> DistrictService:
    return DistrictService(DistrictRepository(db), AreaRepository(db))


def get_district_by_state_service(db: Session = Depends(get_db)) -> DistrictByStateService:
    return DistrictByStateService(DistrictRepository(db), MunicipalityRepository(db), StateRepository(db))


def get_group_gender_service(db: Session = Depends(get_db)) -> GroupGenderService:
    return GroupGenderService(GroupGenderRepository(db))


def get_language_service(db: Session = Depends(get_db)) -> LanguageService:
    return LanguageService(LanguageRepository(db))


def get_group_type_service(db: Session = Depends(get_db)) -> GroupTypeService:
    return GroupTypeService(GroupTypeRepository(db))


def get_group_service(db: Session = Depends(get_db)) -> GroupService:
    return GroupService(GroupRepository(db))


def get_group_by_district_service(db: Session = Depends(get_db)) -> GroupByDistrictService:
    return GroupByDistrictService(GroupRepository(db), DistrictRepository(db))


def get_group_by_state_service(db: Session = Depends(get_db)) -> GroupByStateService:
    return GroupByStateService(GroupRepository(db), MunicipalityRepository(db), StateRepository(db))


def get_evento_service(db: Session = Depends(get_db)) -> EventoService:
    return EventoService(EventoRepository(db))


def get_reflexion_service(db: Session = Depends(get_db)) -> ReflexionService:
    return ReflexionService(ReflexionRepository(db))
