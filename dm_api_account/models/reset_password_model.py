from pydantic import BaseModel, StrictStr, Extra, Field
from typing import Optional


# class ResetPasswordModel(BaseModel):
#     login: StrictStr
#     email: StrictStr


class ResetPassword(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(None, description='Login')
    email: Optional[StrictStr] = Field(None, description='Email')
