from sqlmodel import Field, SQLModel


class Event(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    event_id: str = Field(index=True, unique=True)
    event_type: str
    payload: str
    status: str = Field(default="pending")
    retries: int = Field(default=0)
