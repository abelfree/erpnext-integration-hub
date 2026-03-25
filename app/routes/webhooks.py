from __future__ import annotations

import json

from fastapi import APIRouter, HTTPException
from sqlmodel import select

from app.models.event import Event
from app.services.db import get_session, init_db

router = APIRouter(prefix="/webhooks")
init_db()


@router.post("/order-created")
def order_created(payload: dict):
    event_id = payload.get("event_id")
    if not event_id:
        raise HTTPException(status_code=400, detail="event_id is required")

    with get_session() as session:
        existing = session.exec(select(Event).where(Event.event_id == event_id)).first()
        if existing:
            return {"accepted": True, "duplicate": True}

        evt = Event(event_id=event_id, event_type="order-created", payload=json.dumps(payload))
        session.add(evt)
        session.commit()

    return {"accepted": True, "duplicate": False}
