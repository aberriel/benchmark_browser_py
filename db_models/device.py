# -*- coding: utf-8 -*-

from .db_base import DB_Base


class Device(DB_Base):
    __tablename__ = 'device'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
