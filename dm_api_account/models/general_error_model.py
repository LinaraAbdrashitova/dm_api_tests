from pydantic import BaseModel, Extra, Field, StrictStr
from typing import Any, Dict, List, Optional


class GeneralError(BaseModel):
    class Config:
        extra = Extra.forbid

    message: Optional[StrictStr] = Field(None, description='Client message')
