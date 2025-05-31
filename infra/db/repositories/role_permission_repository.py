from typing import Any, Coroutine, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from domain.dtos.role_permission_dto import RolePermissionDTO
from infra.db.models.role_permission import RolePermission

class RolPermissionRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, dto: RolePermissionDTO) -> RolePermission:
        entity = RolePermission(
            id_rol=dto.id_rol,
            id_permission=dto.id_permission
        )
        self.db.add(entity)
        await self.db.commit()
        await self.db.refresh(entity)
        return entity

    async def get_all(self) -> Sequence[RolePermission]:
        result = await self.db.execute(select(RolePermission))
        return result.scalars().all()

    async def delete(self, id_rol_permission: int) -> None:
        result = await self.db.execute(select(RolePermission).filter_by(id_rol_Permission=id_rol_permission))
        entity = result.scalars().first()
        if entity:
            await self.db.delete(entity)
            await self.db.commit()
