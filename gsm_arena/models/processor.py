# -*- coding: utf-8 -*-

from .gpu import GPU
from commons.models import (
    Brand,
    Manufacturer)


class Processor:
    def __init__(self, manufacturer: Manufacturer = None,
                 brand: Brand = None,
                 model_code: str = None,
                 model_name: str = None,
                 launch_date: date = None,
                 core_counter: int = None,
                 threads: int = None,
                 description: str = None,
                 lithograhp: int = None,
                 hyperthreading: bool = None,
                 overclocking: bool = None,
                 A_core_counter: int = None,
                 A_clock: float = None,
                 B_core_counter: int = None,
                 B_clock: float = None,
                 gpu: GPU = None):
        self.manufacturer = manufacturer
        self.brand = brand
        self.model_code = model_code
        self.model_name = model_name
        self.launch_date = launch_date
        self.core_counter = core_counter
        self.threads = threads
        self.description = description
        self.lithograph = lithograph
        self.hyperthreading = hyperthreading
        self.overclocking = overclocking
        self.A_core_counter = A_core_counter
        self.A_clock = A_clock
        self.B_core_counter = B_core_counter
        self.B_clock = B_clock
        self.gpu = gpu
