from pydantic import Field
from typing import Optional, List

from .node import Node
from .topic import Topic


class Module(Node):
    """Sub-divisão (unidade) de uma disciplina"""

    title: Optional[str] = Field(default=None)
    summary: Optional[str] = Field(default=None)
    number: Optional[int] = Field(
        default=None, description="Número e ordem da unidade dentro da disciplina"
    )
    total_meets: Optional[int] = Field(
        default=None, description="Quantidade de encontros planejados"
    )

    topics: List[Topic] = Field(default_factory=list)
