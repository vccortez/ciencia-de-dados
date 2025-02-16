from pydantic import Field
from typing import Optional, List

from .node import Node
from .topic import Topic

class Module(Node):
    """A unit module of a course"""
    title: Optional[str] = Field(default=None, description="Module title")
    summary: Optional[str] = Field(default=None, description="Module summary")
    number: Optional[int] = Field(..., description="Module number (order within a course)")
    total_sessions: Optional[int] = Field(default=None, description="Number of planned sessions in the module")

    topics: List[Topic] = Field(default_factory=list, description="List of major topics in the module")
