from fastapi import FastAPI, Request
from meli import obtener_token, simular_envio

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Servidor Autoazur + Mercado Libre funcionando"}

@app.get("/auth/init")
def auth_init():
    url = obtener_token()
    return {"authorize_url": url}

@app.get("/auth/callback")
def auth_callback(code: str):
    # Aquí se obtiene y guarda el token usando el código de Mercado Libre
    token = "TOKEN_SIMULADO"  # reemplazar con función real luego
    return {"message": "Token obtenido correctamente", "token": token}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    # Aquí recibirás los webhooks de Mercado Libre
    print("Webhook recibido:", data)
    return {"status": "ok"}

@app.get("/simular")
def simular(precio: float):
    envio, comision, ganancia_neta = simular_envio(precio)
    return {
        "precio": precio,
        "envio": envio,
        "comision": comision,
        "ganancia_neta": ganancia_neta
    }