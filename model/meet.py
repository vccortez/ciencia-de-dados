from pydantic import Field
from typing import Optional
from datetime import datetime

from .node import Node


class Meet(Node):
    """Encontro (aula) para um tópico"""

    content: Optional[str] = Field(default=None)
    date: Optional[datetime] = Field(default=None)
