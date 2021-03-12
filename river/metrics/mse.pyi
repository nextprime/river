from . import base
from typing import Any

class MSE(base.MeanMetric, base.RegressionMetric): ...

class RMSE(MSE):
    def get(self): ...

class RMSLE(RMSE):
    def update(self, y_true: Any, y_pred: Any, sample_weight: float = ...): ...
