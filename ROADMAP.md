# Roadmap

## Next Milestones
- Add HMAC signature validation for webhook security
- Add RabbitMQ/Redis queue backend for scalable workers
- Add observability stack (structured logs + metrics)
- Add OpenAPI examples for external integrator onboarding

## Known Limitations
- SQLite storage is intended for demo/local usage
- Retry policy is fixed and not externally configurable yet
- Single endpoint flow currently focused on order-created events
