from sqlalchemy import select, update, func, delete
from sqlalchemy.ext.asyncio import AsyncSession

from models import Admin


async def orm_add_admin(session: AsyncSession, admin: Admin):
    session.add(admin)
    await session.commit()


async def orm_get_admin(session: AsyncSession, username: str):
    query = select(Admin).where(Admin.username == username)
    result = await session.execute(query)
    return result.scalar()


async def orm_get_all_admins(session: AsyncSession):
    query = select(Admin)
    result = await session.execute(query)
    return result.scalars().all()


async def orm_update_admin(session: AsyncSession, admin: Admin):
    query = update(Admin).where(Admin.username == admin.username).values(
        telegram_id=admin.telegram_id,
        full_name=admin.full_name
    )
    await session.execute(query)
    await session.commit()


async def orm_delete_admin(session: AsyncSession, username: str):
    query = delete(Admin).where(Admin.username == username)
    await session.execute(query)
    await session.commit()

