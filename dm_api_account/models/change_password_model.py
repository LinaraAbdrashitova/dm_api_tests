from pydantic import BaseModel, StrictStr, Field, Extra
from typing import Optional
from uuid import UUID


class ChangePassword(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(None, description='User login')
    token: Optional[UUID] = Field(None, description='Password reset token')
    old_password: Optional[StrictStr] = Field(
        None, alias='oldPassword', description='Old password'
    )
    new_password: Optional[StrictStr] = Field(
        None, alias='newPassword', description='New password'
    )


# class ChangePasswordModel(BaseModel):
#     login: StrictStr
#     token: StrictStr
#     old_password: StrictStr = Field(alias="oldPassword")
#     new_password: StrictStr = Field(alias="newPassword")
