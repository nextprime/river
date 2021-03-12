import typing
from river import base

def expand_param_grid(model: base.Estimator, grid: dict) -> typing.List[base.Estimator]: ...
