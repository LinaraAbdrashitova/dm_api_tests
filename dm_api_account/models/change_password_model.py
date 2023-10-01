from pydantic import BaseModel, StrictStr, Field, Extra
from typing import Optional
from uuid import UUID


class ChangePassword(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(None, description='User login')
    token: Optional[StrictStr] = Field(None, description='Password reset token')
    oldPassword: Optional[StrictStr] = Field(
        None, alias='old_password', description='Old password'
    )
    newPassword: Optional[StrictStr] = Field(
        None, alias='new_password', description='New password'
    )


# class ChangePasswordModel(BaseModel):
#     login: StrictStr
#     token: StrictStr
#     old_password: StrictStr = Field(alias="oldPassword")
#     new_password: StrictStr = Field(alias="newPassword")
