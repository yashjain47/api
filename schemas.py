from enum import Enum
from pydantic import BaseModel


class GenreURLChoices(Enum):
    ROCK = 'rock'
    ELECTRONIC = 'electronic'
    METAL = 'metal'
    HIP_HOP = 'hip-hop'

class Band(BaseModel):
    id : int
    name: str
    genre : str
    