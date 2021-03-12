import sqlalchemy
import typing
from river import base

def iter_sql(query: typing.Union[str, sqlalchemy.sql.expression.Selectable], conn: sqlalchemy.engine.Connectable, target_name: str=...) -> base.typing.Stream: ...
