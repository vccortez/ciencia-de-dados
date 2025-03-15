from typing import Optional, List, Literal
from pydantic import Field

from .node import Node


RKind = Literal["text", "bib", "file", "video", "link"]


class Resource(Node):
    """Recurso arbitrário da disciplina"""

    title: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    value: Optional[str] = Field(default=None)
    kind: Optional[RKind] = Field(default="text")
