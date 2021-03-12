import abc
import pandas as pd
from . import estimator as estimator
from river import base as base
from typing import Any

class Regressor(estimator.Estimator, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def learn_one(self, x: dict, y: base.typing.RegTarget, **kwargs: Any) -> Regressor: ...
    @abc.abstractmethod
    def predict_one(self, x: dict) -> base.typing.RegTarget: ...

class MiniBatchRegressor(Regressor, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def learn_many(self, X: pd.DataFrame, y: pd.Series, **kwargs: Any) -> MiniBatchRegressor: ...
    @abc.abstractmethod
    def predict_many(self, X: pd.DataFrame) -> pd.Series: ...
