# -*- coding: utf-8 -*-

class WiFi:
    def __init__(self, manufacturer: Manufacturer = None,
                 brand: Brand = None,
                 model: str = None,
                 a: bool = False,
                 b: bool = False,
                 g: bool = False,
                 n: bool = False,
                 ac: bool = False,
                 v6: bool = False,
                 v6e: bool = False,
                 v7: bool = False,
                 dual_band: bool = False,
                 tri_band: bool = False,
                 hotspot: bool = False,
                 wifi_direct: bool = False):
        self.manufacturer = manufacturer
        self.brand = brand
        self.model = model
        self.a = a
        self.b = b
        self.g = g
        self.n = n
        self.ac = ac
        self.v6 = v6
        self.v6e = v6e
        self.v7 = v7
        self.dual_band = dual_band
        self.tri_band = tri_band
        self.hotspot = hotspot
        self.wifi_direct = wifi_direct
