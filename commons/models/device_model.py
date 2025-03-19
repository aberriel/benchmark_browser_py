# -*- coding: utf-8 -*-


class DeviceModel:
    def __init__(self, manufacturer: Manufacturer = None,
                 brand: Brand = None,
                 model_name: str = None,
                 model_code: str = None,
                 model_version: str = None):
        self.manufacturer = manufacturer
        self.brand = brand
        self.model_name = model_name
        self.model_code = model_code
        self.model_version = model_version
