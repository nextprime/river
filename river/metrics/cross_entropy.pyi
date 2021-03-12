from . import base

class CrossEntropy(base.MeanMetric, base.MultiClassMetric):
    @property
    def bigger_is_better(self): ...
    @property
    def requires_labels(self): ...
