from datetime import datetime

from sqlalchemy import Column, String, DateTime, ForeignKey, JSON, Integer, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now(), onupdate=datetime.now())


class Admin(Base):
    __tablename__ = 'admins'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    full_name = Column('fullname', String)
    username = Column('username', String)
    telegram_id = Column('telegram_id', Integer)


