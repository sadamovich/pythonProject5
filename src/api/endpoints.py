from typing import List

from fastapi import Query, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from .router import router
from ..types import UserForm
from ..database import User
from ..models import Runner
from ..schemas import RunnerSchema


@router.post('/register')
async def register(form: UserForm):
    form.hash()
    async with User.session() as session:
        user = User(**form.dict())
        session.add(user)
        try:
            await session.commit()
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='email is not unique')
        else:
            raise HTTPException(status_code=status.HTTP_202_ACCEPTED, detail='success')


@router.get('/runner', response_model=List[RunnerSchema])
async def runner(category_id: int = Query(default=None)):
    async with Runner.session() as session:
        if category_id:
            runners = await session.scalars(
                select(Runner)
                .filter_by(category_id=category_id)
                .order_by(Runner.name)
            )
        else:
            runners = await session.scalars(
                select(Runner)
                .order_by(Runner.name)
            )
        return [RunnerSchema.from_orm(runner) for runner in runners]
