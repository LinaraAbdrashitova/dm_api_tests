from pydantic import BaseModel, StrictStr

#change_email_model = {
#    "login": "consectetur aliqua ipsum exercitation ex",
#    "password": "voluptate esse sunt consequat",
#    "email": "velit aliquip tempor aliqua"
#}

class ChangeEmailModel(BaseModel):
    login: StrictStr
    password: StrictStr
    email: StrictStr