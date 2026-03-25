# ERPNext Integration Hub

[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Integration middleware for syncing third-party systems with ERPNext through webhooks, retries, and status tracking.

## Author
Abel Takele

## What This Project Demonstrates
- Webhook ingestion design
- Idempotent event handling
- Async outbound calls to ERPNext REST API
- Retry strategy and failure state management

## Key Features
- `POST /webhooks/order-created` to accept external order events
- Event de-duplication using `event_id`
- `POST /jobs/process` batch processor for ERPNext sync
- Retry counter with `failed` terminal state after max attempts
- `GET /health` operational health endpoint

## Architecture
- `app/main.py`: FastAPI app bootstrap
- `app/routes/webhooks.py`: webhook receiver and event persistence
- `app/routes/jobs.py`: background-like job processing API
- `app/services/erpnext_client.py`: outbound ERPNext API client
- `app/models/event.py`: event state model

## Run Locally
```bash
docker compose up --build
```

## Demo Flow
1. Send webhook payload to `/webhooks/order-created`.
2. Trigger `/jobs/process`.
3. Confirm processed or retried status transitions in event storage.

## Recruiter Notes
This repository demonstrates real integration engineering patterns commonly required in ERP deployments.
