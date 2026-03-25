from __future__ import annotations

import json

from fastapi import APIRouter
from sqlmodel import select

from app.models.event import Event
from app.services.db import get_session
from app.services.erpnext_client import ERPNextClient

router = APIRouter(prefix="/jobs")


@router.post("/process")
async def process_jobs(batch_size: int = 20):
    client = ERPNextClient()
    processed = 0
    failed = 0

    with get_session() as session:
        events = session.exec(
            select(Event).where(Event.status == "pending").limit(batch_size)
        ).all()

        for evt in events:
            try:
                payload = json.loads(evt.payload)
                await client.create_sales_order(payload["sales_order"])
                evt.status = "processed"
                processed += 1
            except Exception:
                evt.retries += 1
                evt.status = "failed" if evt.retries >= 3 else "pending"
                failed += 1

        session.add_all(events)
        session.commit()

    return {"processed": processed, "failed": failed}
