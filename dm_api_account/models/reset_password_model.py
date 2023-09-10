from pydantic import BaseModel, StrictStr

#reset_password_model = {
#    "login": "nostrud exercitation laborum c",
#    "email": "adipisicing"
#}
class ResetPasswordModel(BaseModel):
    login: StrictStr
    email: StrictStr