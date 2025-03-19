# -*- coding: utf-8 -*-

from .country import Country


class Manufacturer:
    def __init__(self, name: str, country: Country = None, website: str = None):
        self.name = name
        self.country = country
        self.website = website
