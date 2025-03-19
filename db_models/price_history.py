# -*- coding: utf-8 -*-

from .db_base import DB_Base
from .device import Device

from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import (Mapped, mapped_column, relationship)


class PriceHistory(DB_Base):
	__tablename__ = 'price_history'

	id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
	price
	source_name
	source_url
	store_name
	store_url
	collect_date
