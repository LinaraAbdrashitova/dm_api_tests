from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class Rating(BaseModel):
    enabled: bool
    quality: int
    quantity: int
class BbParseMode(str, Enum):
    COMMON = "Common"
    INFO = "Info"
    POST = "Post"
    CHAT = "Chat"

class InfoBbText(BaseModel):
    value: str = Field(None)
    parse_mode: BbParseMode


class Paging(BaseModel):
    posts_per_page: int = Field(..., alias='postsPerPage')
    comments_per_page: int = Field(..., alias='commentsPerPage')
    topics_per_page: int = Field(..., alias='topicsPerPage')
    messages_per_page: int = Field(..., alias='messagesPerPage')
    entities_per_page: int = Field(..., alias='entitiesPerPage')

class ColorSchema(str, Enum):
    MODERN = "Modern"
    PALE = "Pale"
    CLASSIC = "Classic"
    CLASSICPALE = "ClassicPale"

class UserSettings(BaseModel):
    color_schema: ColorSchema = Field(alias='colorSchema')
    nanny_greetings_message: str = Field(None, alias='nannyGreetingsMessage')
    paging: Paging

class UserRole(str, Enum):
    GUEST = "Guest"
    PLAYER = "Player"
    ADMINISTRATOR = "Administrator"
    NANNY_MODERATOR = "NannyModerator"
    REGULAR_MODERATOR = "RegularModerator"
    SENIOR_MODERATOR = "SeniorModerator"


class UserDetails(BaseModel):
    login: str
    roles: List[UserRole]
    medium_picture_url: str = Field(None, alias='mediumPictureUrl')
    small_picture_url: str = Field(None, alias='smallPictureUrl')
    status: str = Field(None, alias='status')
    rating: Rating
    online: datetime = Field(None, alias='online')
    name: str = Field(None, alias="name")
    location: str = Field(None, alias="location")
    registration: datetime = Field(None, alias="registration")
    icq: str = Field(None)
    skype: str = Field(None)
    original_picture_url: str = Field(None, alias='originalPictureUrl')
    info: str = Field(None)
    settings: UserSettings


class UserDetailsEnvelope(BaseModel):
    model_config = ConfigDict(extra="forbid")
    resource: Optional[UserDetails] = None
    metadata: Optional[str] = None
