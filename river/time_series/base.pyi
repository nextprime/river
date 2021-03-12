import abc
from .. import base as base

class Forecaster(base.Estimator, metaclass=abc.ABCMeta):
    def learn_one(self, y: float, x: dict=...) -> Forecaster: ...
    @abc.abstractmethod
    def forecast(self, horizon: int, xs: list=...) -> list: ...
