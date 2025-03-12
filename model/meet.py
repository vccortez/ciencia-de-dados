import os
from pathlib import Path

from pydantic import Field, computed_field
from typing import Optional, List, Union
from datetime import date

from .node import Node


class Meet(Node):
    """Encontro sobre um ou mais tópicos"""

    title: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    res_base_path: Path = Field(
        default=Path(os.path.dirname(os.path.realpath(__file__))).parent
    )
    resources: List[str] = Field(default_factory=list)

    is_extra: Optional[bool] = Field(default=False)
    is_canceled: Optional[bool] = Field(default=False)

    has_content: Optional[bool] = Field(default=True)
    is_exam: Optional[bool] = Field(default=False)
    is_closing: Optional[bool] = Field(default=False)

    start_date: Optional[date] = Field(default=None)
    date_span: Optional[int] = Field(default=1)
    dates: List[date] = Field(default_factory=list)

    topics: List[str] = Field(default_factory=list)
    module_number: Optional[int] = Field(default=1)

    @computed_field
    def res_paths(self) -> List[Path]:
        return [
            fpath
            for rpath in self.resources
            if (fpath := self.res_base_path / rpath) and fpath.exists and fpath.is_file
        ]
