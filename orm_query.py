from sqlalchemy import select, update, func
from sqlalchemy.ext.asyncio import AsyncSession

from models import Admin


async def orm_add_admin(session: AsyncSession, admin: Admin):
    session.add(admin)
    await session.commit()


async def orm_get_admin(session: AsyncSession, id: int):
    query = select(Admin).where(Admin.id == id)
    result = await session.execute(query)
    return result.scalar()


async def orm_get_all_admins(session: AsyncSession):
    query = select(Admin)
    result = await session.execute(query)
    return result.scalars().all()

