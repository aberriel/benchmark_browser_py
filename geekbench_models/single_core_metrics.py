# -*- coding: utf-8 -*-

from .benchmark_metric import BenchmarkMetric


class SingleCoreMetrics:
    def __init__(self, general_score: int = None,
                 file_compression: BenchmarkMetric = None,
                 navigation: BenchmarkMetric = None,
                 html5_browser: BenchmarkMetric = None,
                 pdf_renderer: BenchmarkMetric = None,
                 photo_library: BenchmarkMetric = None,
                 clang: BenchmarkMetric = None,
                 text_processing: BenchmarkMetric = None,
                 asset_compression: BenchmarkMetric = None,
                 object_detection: BenchmarkMetric = None,
                 backgroung_blur: BenchmarkMetric = None,
                 horizon_detection: BenchmarkMetric = None,
                 object_Remover: BenchmarkMetric = None,
                 hdr: BenchmarkMetric = None,
                 photo_filter: BenchmarkMetric = None,
                 ray_tracer: BenchmarkMetric = None,
                 structure_from_motion: BenchmarkMetric = None):
        self.general_score = general_score
        self.file_compression = file_compression
        self.navigation = navigation
