import abc
from . import base as base
from typing import Any

class Estimator(base.Base, abc.ABC):
    def __or__(self, other: Any): ...
    def __ror__(self, other: Any): ...
