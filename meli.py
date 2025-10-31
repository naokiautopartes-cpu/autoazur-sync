import random

def obtener_token():
    """
    Devuelve la URL para autorizar la app de Mercado Libre.
    Recuerda reemplazar TU_APP_ID y TU_REDIRECT_URI por tus datos reales.
    """
    return "https://auth.mercadolibre.com/authorization?client_id=TU_APP_ID&response_type=code&redirect_uri=TU_REDIRECT_URI"

def simular_envio(precio):
    """
    Simula el costo de envío y comisión.
    Retorna: envio, comision, ganancia_neta
    """
    costos_envio = [87.5, 95, 110, 165]
    envio = random.choice(costos_envio)
    comision = precio * 0.13  # ejemplo de comisión Mercado Libre
    ganancia_neta = precio - comision - envio
    return envio, comision, ganancia_neta