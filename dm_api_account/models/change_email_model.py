from pydantic import BaseModel, StrictStr, Extra, Field
from typing import Optional

class ChangeEmail(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(None, description='User login')
    password: Optional[StrictStr] = Field(None, description='User password')
    email: Optional[StrictStr] = Field(None, description='New user email')

# class ChangeEmailModel(BaseModel):
#     login: StrictStr
#     password: StrictStr
#     email: StrictStr