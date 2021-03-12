import numpy as np
import typing
from river import base as base

def iter_array(X: np.ndarray, y: np.ndarray=..., feature_names: typing.List[base.typing.FeatureName]=..., target_names: typing.List[base.typing.FeatureName]=..., shuffle: bool=..., seed: int=...) -> base.typing.Stream: ...
