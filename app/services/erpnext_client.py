from __future__ import annotations

import os

import httpx


class ERPNextClient:
    def __init__(self):
        self.base_url = os.getenv("ERPNEXT_URL", "http://erpnext:8000")
        self.api_key = os.getenv("ERPNEXT_API_KEY", "demo_key")
        self.api_secret = os.getenv("ERPNEXT_API_SECRET", "demo_secret")

    async def create_sales_order(self, payload: dict):
        headers = {
            "Authorization": f"token {self.api_key}:{self.api_secret}",
            "Content-Type": "application/json",
        }
        async with httpx.AsyncClient(timeout=20) as client:
            response = await client.post(
                f"{self.base_url}/api/resource/Sales Order", headers=headers, json=payload
            )
            response.raise_for_status()
            return response.json()
