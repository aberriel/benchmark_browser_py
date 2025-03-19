# -*- coding: utf-8 -*-

class MobileNetwork:
    def __init__(self, sim: bool = False, sim_type: SimType = None,
                 bands_2g_gsm: list = [],
                 bands_2g_cdma: list = [],
                 bands_3g_hsdpa: list = [],
                 bands_3g_evdo: list = [],
                 bands_4g_lte: list = [],
                 bands_5g: list = [],
                 speed_2g: float = None,
                 speed_3g: float = None,
                 speed_4g: float = None,
                 speed_5g: float = None):
        self.sim = sim
        self.sim_type = sim_type
        self.bands_2g_gsm = bands_2g_gsm
        self.bands_2g_cdma = bands_2g_cdma
        self.bands_3g_hsdpa = bands_3g_hsdpa
        self.bands_3g_evdo = bands_3g_evdo
        self.bands_4g_lte = bands_4g_lte
        self.bands_5g = bands_5g
        self.speed_2g = speed_2g
        self.speed_3g = speed_3g
        self.speed_4g = speed_4g
        self.speed_5g = speed_5g
