from pydantic import BaseModel, StrictStr, Field, Extra
from datetime import datetime
from typing import List, Optional, Any
from enum import Enum


# class UserRole(Enum):
#     GUEST = "Guest"
#     PLAYER = "Player"
#     ADMINISTRATOR = "Administrator"
#     NANNY_MODERATOR = "NannyModerator"
#     REGULAR_MODERATOR = "RegularModerator"
#     SENIOR_MODERATOR = "SeniorModerator"
#
#
# class Rating(BaseModel):
#     enabled: bool
#     quality: int
#     quantity: int
#
#
# class User(BaseModel):
#     login: StrictStr
#     roles: List[UserRole]
#     medium_picture_url: Optional[StrictStr] = Field(None, alias="mediumPictureUrl")
#     small_picture_url: Optional[StrictStr] = Field(None, alias="smallPictureUrl")
#     status: Optional[StrictStr] = None
#     rating: Rating
#     online: Optional[datetime] = None
#     name: Optional[StrictStr] = None
#     location: Optional[StrictStr] = None
#     registration: Optional[datetime] = None

class Rating(BaseModel):
    class Config:
        extra = Extra.forbid

    enabled: Optional[bool] = Field(None, description='Rating participation flag')
    quality: Optional[int] = Field(None, description='Quality rating')
    quantity: Optional[int] = Field(None, description='Quantity rating')


class UserRole(Enum):
    GUEST = "Guest"
    PLAYER = "Player"
    ADMINISTRATOR = "Administrator"
    NANNY_MODERATOR = "NannyModerator"
    REGULAR_MODERATOR = "RegularModerator"
    SENIOR_MODERATOR = "SeniorModerator"


class User(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(None, description='Login')
    roles: Optional[List[UserRole]] = Field(None, description='Roles')
    medium_picture_url: Optional[StrictStr] = Field(
        None, alias='mediumPictureUrl', description='Profile picture URL M-size'
    )
    small_picture_url: Optional[StrictStr] = Field(
        None, alias='smallPictureUrl', description='Profile picture URL S-size'
    )
    status: Optional[StrictStr] = Field(None, description='User defined status')
    rating: Optional[Rating] = None
    online: Optional[datetime] = Field(None, description='Last seen online moment')
    name: Optional[StrictStr] = Field(None, description='User real name')
    location: Optional[StrictStr] = Field(None, description='User real location')
    registration: Optional[datetime] = Field(
        None, description='User registration moment'
    )


class UserEnvelope(BaseModel):
    class Config:
        extra = Extra.forbid

    resource: Optional[User] = None
    metadata: Optional[Any] = Field(None, description='Additional metadata')
