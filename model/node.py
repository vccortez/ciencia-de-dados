from pydantic import BaseModel, ConfigDict


class Node(BaseModel):
    """Base class for shared config across models"""

    model_config = ConfigDict(populate_by_name=True, extra='allow')
