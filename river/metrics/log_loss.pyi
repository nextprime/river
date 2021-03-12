from . import base

class LogLoss(base.MeanMetric, base.BinaryMetric):
    @property
    def bigger_is_better(self): ...
    @property
    def requires_labels(self): ...
