from fastapi import APIRouter, Response
from glogger.logger import get_logger
from copy_trader import models
import time

router = APIRouter()
logger = get_logger("routes")

events: list[models.Event] = []


@router.get("/health")
def health() -> dict:
    """
    Health check
    """
    logger.info("alive")
    return {
        "message": "alive",
        "events-cnt": len(events),
        "timestamp": int(time.time()),
    }


@router.post("/signal")
def signal(
    data: models.Signal,
    # symbol: str, timeframe: int, price: float, stop_loss: float
) -> models.Signal:
    """
    New signal
    """
    logger.info(
        "New signal %s %f %f %f %s %s",
        data.symbol,
        data.risk,
        data.price,
        data.stop_loss,
        data.market,
        data.buy,
    )
    # data = models.Signal(symbol=symbol, timeframe=timeframe, price=price, stop_loss=stop_loss)
    events.append(models.Event(type=models.EventType.SIGNAL, data=data))
    return data


@router.delete("/signal")
def delete_position(
    data: models.Delete,
    # symbol: str, timeframe: int
) -> models.Delete:
    """
    Close position signal
    """
    logger.info("Closing position %d", data.id)
    # data = models.Delete(symbol=symbol, timeframe=timeframe)
    events.append(models.Event(type=models.EventType.CLOSE_POSITION, data=data))
    return data


@router.put("/signal")
def edit_sltp(data: models.Edit) -> models.Edit:
    """
    Edits tp and sl
    """
    logger.info("Edit position %d %f %f", data.id, data.stop_loss, data.take_profit)
    events.append(models.Event(type=models.EventType.EDIT_POSITION, data=data))


@router.get("/events")
def events_count() -> int:
    """
    Counts number of events
    """
    return len(events)


@router.get("/get_event")
def new_event(pos: int) -> None | models.Event:
    """
    Gets event by position (index)
    """
    if pos >= len(events):
        return Response(status_code=404)
    return events[pos]
