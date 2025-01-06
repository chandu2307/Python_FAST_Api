"""
Source code : Car Model
"""

from typing import List,Optional
from pydantic import BaseModel , Field

class CarModel(BaseModel):
    """
     CarModel using pydantic
    """

    make : Optional[str]
    model : Optional[str]
    year : Optional[int] = Field(...,ge=970,le=2025)
    price : Optional[float]
    engine : Optional[str] = "V4" #default is v4
    autonomous : Optional[bool]
    sold : Optional[List[str]]

