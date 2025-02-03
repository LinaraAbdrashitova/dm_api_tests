from pydantic import BaseModel, Field, ConfigDict


class ChangePassword(BaseModel):
    model_config = ConfigDict(extra="forbid")
    login: str = Field(..., description='Логин')
    token: str = Field(..., description='Токен')
    old_password: str = Field(..., serialization_alias='oldPassword', description='Старый пароль')
    new_password: str = Field(..., serialization_alias='newPassword', description='Новый пароль')

