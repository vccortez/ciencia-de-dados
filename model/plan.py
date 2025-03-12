from pydantic import Field
from typing import List

from .node import Node
from .meet import Meet


class Plan(Node):
    meets: List[Meet] = Field(default_factory=list)
