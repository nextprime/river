import datetime as dt
import typing
from river import base, metrics
from typing import Any

def progressive_val_score(dataset: base.typing.Stream, model: Any, metric: metrics.Metric, moment: typing.Union[str, typing.Callable]=..., delay: typing.Union[str, int, dt.timedelta, typing.Callable]=..., print_every: Any=..., show_time: Any=..., show_memory: Any=..., **print_kwargs: Any) -> metrics.Metric: ...
