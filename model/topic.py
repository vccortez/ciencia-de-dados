from pydantic import Field
from typing import Optional, List

from .node import Node
from .meet import Meet


class Topic(Node):
    """Tópico de uma unidade"""

    name: Optional[str] = Field(default=None)
    subject: Optional[str] = Field(default=None)
    total_meets: Optional[int] = Field(default=1)
    is_exam: Optional[bool] = Field(default=False)

    meets: List[Meet] = Field(default_factory=list)
    res: List[str] = Field(default_factory=list)
