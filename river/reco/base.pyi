import abc
from river import base as base
from typing import Any

class Recommender(base.Regressor, metaclass=abc.ABCMeta):
    def learn_one(self, x: Any, y: Any): ...
    def predict_one(self, x: Any): ...
