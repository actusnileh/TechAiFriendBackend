from fastapi.routing import APIRouter


router = APIRouter(tags=["Help"], prefix="/help")


@router.get(
    "",
    summary="Получить справку по работе с API",
)
def get_help():
    return "test"
