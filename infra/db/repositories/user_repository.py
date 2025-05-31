from typing import Any, Coroutine, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from domain.dtos.user_dto import UserDTO
from infra.db.models.user import User

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, dto: UserDTO) -> User:
        user = User(
            tipe_document=dto.tipe_document,
            number_document=dto.number_document,
            name=dto.name,
            last_name=dto.last_name,
            phone=dto.phone,
            adress=dto.address,
            date_of_birth=dto.date_of_birth,
            email=dto.email,
            password=dto.password,
            date_registration=dto.date_registration,
            active=dto.active
        )
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def get_by_id(self, id_user: int) -> User:
        result = await self.db.execute(select(User).filter_by(id_user=id_user))
        return result.scalars().first()

    async def list_all(self) -> Sequence[User]:
        result = await self.db.execute(select(User))
        return result.scalars().all()

    async def delete(self, id_user: int) -> None:
        result = await self.db.execute(select(User).filter_by(id_user=id_user))
        user = result.scalars().first()
        if user:
            await self.db.delete(user)
            await self.db.commit()
