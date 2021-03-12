import abc
from . import estimator as estimator

class Clusterer(estimator.Estimator, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def learn_one(self, x: dict) -> Clusterer: ...
    @abc.abstractmethod
    def predict_one(self, x: dict) -> int: ...
