# ERPNext Integration Hub

Middleware service for third-party integrations with ERPNext.

## Use Case
Sync orders/customers/payments from external commerce tools into ERPNext with retries and logs.

## Features
- Webhook receiver endpoint
- Idempotent event storage
- Retry queue for failed outbound syncs
- ERPNext REST API client
- Healthcheck and structured logs

## Run
```bash
docker compose up --build
```

## Endpoints
- `POST /webhooks/order-created`
- `POST /jobs/process`
- `GET /health`
