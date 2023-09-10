from pydantic import BaseModel, StrictStr, Field, StringConstraints
from datetime import datetime
from typing import List, Optional
from enum import Enum


class UserRole(Enum):
    GUEST = "Guest"
    PLAYER = "Player"
    ADMINISTRATOR = "Administrator"
    NANNY_MODERATOR = "NannyModerator"
    REGULAR_MODERATOR = "RegularModerator"
    SENIOR_MODERATOR = "SeniorModerator"


class Rating(BaseModel):
    enabled: bool
    quality: int
    quantity: int


class User(BaseModel):
    login: StrictStr
    roles: List[UserRole]
    medium_picture_url: Optional[StrictStr] = Field(None, alias="mediumPictureUrl")
    small_picture_url: Optional[StrictStr] = Field(None, alias="smallPictureUrl")
    status: Optional[StrictStr] = None
    rating: Rating
    online: Optional[datetime] = None
    name: Optional[StrictStr] = None
    location: Optional[StrictStr] = None
    registration: Optional[datetime] = None


class UserEnvelopeModel(BaseModel):
    resource: User
    metadata: Optional[StrictStr] = None

