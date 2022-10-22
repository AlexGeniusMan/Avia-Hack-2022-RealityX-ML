import typing as tp

from pydantic import BaseModel


class Prediction(BaseModel):
    engine_id: str
    flight_phase: str
    flight_datetime: str
    metrics: tp.Dict[str, tp.Optional[float]]
