# -*- coding: utf-8 -*-

class PerformanceTest:
    def __init__(self, platform_name: str = None,
                 platform_version: str = None,
                 score: int = None):
        self.platform_name = platform_name
        self.platform_version = platform_version
        self.score = score
