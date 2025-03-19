# -*- coding: utf-8 -*-

from .os_family import OS_Family
from .os_type import OS_Type
from datetime import date

class OperationalSystem:
    def __init__(self, family: OS_Family = None,
                 system_type: OS_Type = None,
                 name: str = None,
                 manufacturer: Manufacturer = None,
                 version_number: str = None,
                 version_code: str = None,
                 launch_date: date = None,
                 kernel_version: str = None):
        self.family = family
        self.system_type = system_type
        self.name = name
        self.manufacturer = manufacturer
        self.version_number = version_number
        self.version_code = version_code
        self.launch_date = launch_date
        self.kernel_version = kernel_version
