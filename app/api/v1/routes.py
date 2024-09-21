from fastapi import APIRouter

from app.api.v1.endpoints.help import router as help_router


routers = APIRouter()
router_list = [
    help_router,
]

for router in router_list:
    router.tags = routers.tags.append("v1")
    routers.include_router(router)
