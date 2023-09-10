from pydantic import BaseModel, StrictStr, Field

#change_password_model = {
#            "login": "cillum culpa labore ullamco",
#            "token": "c3ff00bb-76f4-5c6b-5438-32a3ec94cbd1",
#            "oldPassword": "occaecat",
#            "newPassword": "Excepteur cupidatat id"
#        }
class ChangePasswordModel(BaseModel):
    login: StrictStr
    token: StrictStr
    old_password: StrictStr = Field(alias="oldPassword")
    new_password: StrictStr = Field(alias="newPassword")