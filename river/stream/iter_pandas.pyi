import pandas as pd
import typing
from river import base as base, stream as stream
from typing import Any

def iter_pandas(X: pd.DataFrame, y: typing.Union[pd.Series, pd.DataFrame]=..., **kwargs: Any) -> base.typing.Stream: ...
