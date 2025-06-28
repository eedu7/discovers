from fastapi import APIRouter

from api.favicon.favicon import favicon_router
from api.v1 import v1_router

router = APIRouter()

router.include_router(favicon_router)
router.include_router(v1_router, tags=["Home"])
