from pydantic import Field
from typing import Optional, List

from .node import Node

class Topic(Node):
    """A single syllabus topic"""
    name: Optional[str] = Field(default=None)
    subject: Optional[str] = Field(default=None)
    total_sessions: Optional[int] = Field(default=1)