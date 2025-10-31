# Autoazur Sync

Servidor FastAPI para sincronizar Autoazur con Mercado Libre México.

## Endpoints
- `/auth/init` → Genera URL de autorización
- `/auth/callback` → Recibe token de Mercado Libre
- `/webhook` → Recibe webhooks de Mercado Libre
- `/simular` → Simula envío y comisión

## Variables de entorno
Ver `.env.example`