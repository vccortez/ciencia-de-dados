from pydantic import Field
from typing import Optional, List

from .node import Node
from .meet import Meet


class Topic(Node):
    """Tópico de uma unidade"""

    name: Optional[str] = Field(default=None)
    subject: Optional[str] = Field(default=None)
    total_meets: Optional[int] = Field(default=1)

    meets: List[Meet] = Field(default_factory=list)
