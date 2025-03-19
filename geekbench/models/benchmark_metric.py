# -*- coding: utf-8 -*-


class BenchmarkMetric:
    def __init__(self, metric_name: str = None,
                 measure: str = None,
                 score: int = None,
                 tax: float = None):
        self.metric_name = metric_name
        self.measure = measure
        self.score = score
        self.tax = tax
