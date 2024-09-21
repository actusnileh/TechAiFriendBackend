from fastapi import APIRouter

from app.api.v1.endpoints.users import router as users_router


routers = APIRouter()
router_list = [
    users_router,
]

for router in router_list:
    router.tags = routers.tags.append("v1")
    routers.include_router(router)
