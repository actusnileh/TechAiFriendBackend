from fastapi import APIRouter

from app.schema.table_schema import TableNameEnum
from app.services.information_service import InformationService


router = APIRouter(tags=["Information"], prefix="/information")


@router.get(
    "/get_information/{table_name}",
    summary="Получить информацию по таблице в формате CSV",
)
async def get_all_information(table_name: TableNameEnum):
    return await InformationService().get_all_information(table_name)
