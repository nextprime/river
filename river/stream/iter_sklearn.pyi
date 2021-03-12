import sklearn.utils
from river import base as base, stream as stream
from typing import Any

def iter_sklearn_dataset(dataset: sklearn.utils.Bunch, **kwargs: Any) -> base.typing.Stream: ...
