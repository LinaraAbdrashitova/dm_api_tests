from pydantic import BaseModel, StrictStr, Field
from datetime import datetime
from typing import Optional, List
from enum import Enum

class PagingSettings(BaseModel):
    posts_per_page: int = Field(alias="postsPerPage")
    comments_per_page: int = Field(alias="commentsPerPage")
    topics_per_page: int = Field(alias="topicsPerPage")
    messages_per_page: int = Field(alias="messagesPerPage")
    entities_per_page: int = Field(alias="entitiesPerPage")
class ColorSchema(Enum):
    MODERN = "Modern",
    PALE = "Pale",
    CLASSIC = "Classic",
    CLASSIC_PALE = "ClassicPale",
    NIGHT = "Night"


class BbParseMode(Enum):
    COMMON = "Common",
    INFO = "Info",
    POST = "Post",
    CHAT = "Chat"


class UserSettings(BaseModel):
    color_schema: List[ColorSchema] = Field(alias="colorSchema")
    nanny_greetings_message: StrictStr = Field(alias="nannyGreetingsMessage")
    paging: PagingSettings

class UserRole(Enum):
    GUEST = "Guest"
    PLAYER = "Player"
    ADMINISTRATOR = "Administrator"
    NANNY_MODERATOR = "NannyModerator"
    REGULAR_MODERATOR = "RegularModerator"
    SENIOR_MODERATOR = "SeniorModerator"

class InfoBbText(BaseModel):
    value: StrictStr
    parse_mode: List[BbParseMode] = Field(alias="parseMode")


class Rating(BaseModel):
    enabled: bool
    quality: int
    quantity: int


class UserDetails(BaseModel):
    login: StrictStr
    roles: List[UserRole]
    medium_picture_url: StrictStr = Field(alias="mediumPictureUrl")
    small_picture_url: StrictStr = Field(alias="smallPictureUrl")
    status: StrictStr
    rating: Rating
    online: datetime
    name: StrictStr
    location: StrictStr
    registration: datetime
    icq: StrictStr
    skype: StrictStr
    original_picture_url: StrictStr = Field("originalPictureUrl")
    info: InfoBbText
    settings: UserSettings


class UserDetailsEnvelopeModel(BaseModel):
    resource: UserDetails
    metadata: StrictStr