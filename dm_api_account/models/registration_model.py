from pydantic import BaseModel, StrictStr, Extra, Field
from typing import Optional

class Registration(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(None, description='Login')
    email: Optional[StrictStr] = Field(None, description='Email')
    password: Optional[StrictStr] = Field(None, description='Password')


# class RegistrationModel(BaseModel):
#     login: StrictStr
#     email: StrictStr
#     password: StrictStr
