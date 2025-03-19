# -*- coding: utf-8 -*-


class Bluetooth:
    def __init__(self, manufacturer: Manufacturer = None,
                 brand: Brand = None,
                 model: str = None,
                 version: float = None,
                 a2dp: bool = False,
                 le: bool = False):
        self.manufacturer = manufacturer
        self.brand = brand
        self.model = model
        self.version = version
        self.a2dp = a2dp
        self.le = le
