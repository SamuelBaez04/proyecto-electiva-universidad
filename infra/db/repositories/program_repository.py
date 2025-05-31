from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from domain.dtos.program_dto import ProgramDTO
from infra.db.models.program import Program

class ProgramRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, dto: ProgramDTO) -> Program:
        program = Program(**dto.__dict__)
        self.db.add(program)
        await self.db.commit()
        await self.db.refresh(program)
        return program

    async def get_by_id(self, id_program: int) -> Program:
        result = await self.db.execute(select(Program).filter_by(id_program=id_program))
        return result.scalars().first()

    async def list_all(self) -> list[Program]:
        result = await self.db.execute(select(Program))
        return result.scalars().all()

    async def delete(self, id_program: int) -> None:
        result = await self.db.execute(select(Program).filter_by(id_program=id_program))
        entity = result.scalars().first()
        if entity:
            await self.db.delete(entity)
            await self.db.commit()
