from . import base

class SMAPE(base.MeanMetric, base.RegressionMetric):
    def get(self): ...
