# -*- coding: utf-8 -*-

from commons.models import ScreenType


class Screen:
    def __init__(self, s_type: ScreenType,
                 description: str = None,
                 resolution_width: int = 0,
                 resolution_height: int = 0,
                 aspect_ratio: str = None,
                 size_inch: float = None,
                 screen_to_body_ratio: int = None,
                 ppi_density: int = None,
                 brightness_typ: int = None,
                 brightness_peak: int = None,
                 brightness_hbm: int = None,
                 refresh_rate: int = None,
                 dolby_vision: bool = False,
                 hdr_10: bool = False,
                 has_protection: bool = False,
                 protection_description: str = None,
                 has_always_on: bool = False):
        self.s_type = s_type
        self.description = description
        self.resolution_width = resolution_width
        self.resolution_height = resolution_height
        self.aspect_ratio = aspect_ratio
        self.size_inch = size_inch
        self.screen_to_body_ratio = screen_to_body_ratio
        self.ppi_density = ppi_density
        self.brightness_typ = brightness_typ
        self.brightness_peak = brightness_peak
        self.brightness_hbm = brightness_hbm
        self.refresh_rate = refresh_rate
        self.dolby_vision = dolby_vision if dolby_vision is not None else False
        self.hdr_10 = hdr_10 if hdr_10 is not None else False
        self.has_protection = has_protection if has_protection is not None else False
        self.protection_description = protection_description
        self.has_always_on = has_always_on if has_always_on is not None else False
