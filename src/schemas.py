from pydantic.types import Decimal

from .types import Schema


class RunnerSchema(Schema):
    name: str
    surname: str
    description: str
    category_id: int