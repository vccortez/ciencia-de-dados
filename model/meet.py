from pydantic import Field
from typing import Optional, List
from datetime import date

from .node import Node


class Meet(Node):
    """Encontro sobre um ou mais tópicos"""

    title: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    resources: List[str] = Field(default_factory=list)

    content: Optional[bool] = Field(default=True)
    canceled: Optional[bool] = Field(default=False)

    start_date: Optional[date] = Field(default=None)
    date_span: Optional[int] = Field(default=1)

    module_number: Optional[int] = Field(default=1)
    topics: List[str] = Field(default_factory=list)
    dates: List[date] = Field(default_factory=list)
