import abc
from . import estimator as estimator

class AnomalyDetector(estimator.Estimator, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def learn_one(self, x: dict) -> AnomalyDetector: ...
    @abc.abstractmethod
    def score_one(self, x: dict) -> float: ...
