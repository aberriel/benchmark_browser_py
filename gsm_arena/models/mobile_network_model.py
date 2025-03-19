# -*- coding: utf-8 -*-

from .mobile_network import MobileNetwork
from commons.models import (
    Brand,
    Manufacturer)


class MobileNetworkModel:
    def __init__(self, model_code: str = None,
                 sim: bool = False,
                 sim_type: SimType = None,
                 networks: MobileNetwork = None):
        self.model_code = model_code
        self.sim = sim if sim is not None else False
        self.sim_type = sim_type
        self.networks = networks
