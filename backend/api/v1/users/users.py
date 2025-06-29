from fastapi import APIRouter

from app.models import User
from core.database.session import session
from core.database.transactional import Propagation, Transactional
from core.repository.base import BaseRepository

router = APIRouter()


user_crud = BaseRepository(User, session)


@Transactional(propagation=Propagation.REQUIRED)
async def register():
    user_data = {
        "username": "John Doe",
        "email": "john.doe@example.com",
        "password": "password",
    }

    await user_crud.create(user_data)


@router.get("/")
async def create():
    await register()
    return {"message": "Created successfully"}


@router.get("/all")
async def all():
    data = await user_crud.get_all()
    return {"data": data}
