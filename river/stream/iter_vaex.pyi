import typing
import vaex
from river import base as base

def iter_vaex(X: vaex.dataframe.DataFrame, y: typing.Union[str, vaex.expression.Expression]=..., features: typing.Union[typing.List[str], vaex.expression.Expression]=...) -> base.typing.Stream: ...
