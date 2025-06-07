import os
from pathlib import Path
from typing import Union


def relpath(path: str | Path, start: str | Path, to_path=False) -> str | Path:
    """
    Workaround to Path.relative_to(walk_up) in Python 3.10
    """
    res = os.path.relpath(path, start)
    return res if not to_path else Path(res)
