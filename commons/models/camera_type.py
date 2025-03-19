# -*- coding: utf-8 -*-

from enum import Enum


class CameraType(Enum):
    WIDE = 'WIDE'
    TELEPHOTO = 'TELEPHOTO'
    ULTRAWIDE = 'ULTRAWIDE'
    MACRO = 'MACRO'
    SELFIE = 'SELFIE'
    DEPTH = 'DEPTH'
