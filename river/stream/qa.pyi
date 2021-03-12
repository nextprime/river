import datetime as dt
import typing
from river import base
from typing import Any

class Memento:
    def __lt__(self, other: Any) -> Any: ...

def simulate_qa(dataset: base.typing.Stream, moment: typing.Union[str, typing.Callable], delay: typing.Union[str, int, dt.timedelta, typing.Callable], copy: bool=...) -> Any: ...
