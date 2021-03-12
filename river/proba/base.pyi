import abc
from typing import Any

class Distribution(abc.ABC, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, x: Any) -> Any: ...
    @property
    @abc.abstractmethod
    def n_samples(self) -> Any: ...

class DiscreteDistribution(Distribution, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def pmf(self, x: Any) -> Any: ...

class ContinuousDistribution(Distribution, metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def mode(self) -> Any: ...
    @abc.abstractmethod
    def pdf(self, x: Any) -> Any: ...
    @abc.abstractmethod
    def cdf(self, x: Any) -> Any: ...
