from dataclasses import dataclass, field
from pydantic import BaseModel, Field

from enum import IntEnum
import time


class Signal(BaseModel):
    """
    Signal data model
    """

    symbol: str
    price: float
    stop_loss: float
    buy: bool
    market: bool
    id: int
    risk: float


class Delete(BaseModel):
    """
    Delete position signal
    """

    id: int


class Edit(BaseModel):
    """
    Edits position
    """

    id: int
    stop_loss: float = -1
    take_profit: float = -1


class EventType(IntEnum):
    """
    Type of events that happened
    """

    SIGNAL = 0
    CLOSE_POSITION = 1
    EDIT_POSITION = 2


class Event(BaseModel):
    """
    Event class
    """

    type: EventType
    data: Signal | Delete | Edit
    create_timestamp: int = Field(default_factory=lambda: int(time.time()))
