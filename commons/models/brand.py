# -*- coding: utf-8 -*-

from .manufacturer import Manufacturer


class Brand:
    def __init__(self, manufacturer: Manufacturer = None,
                 name: str = None,
                 website: str = None):
        self.manufacturer = manufacturer
        self.name = name
        self.website = website
