import os
import json
import random
from utils.analisis import analizar_emocion

def generar_respuesta(texto_usuario):
    # detectar emociones en el texto del usuario
    emociones_detectadas = analizar_emocion(texto_usuario)

    # construir ruta
    ruta_respuestas = os.path.join(os.path.dirname(__file__), 'respuesta.json')

    with open(ruta_respuestas, 'r', encoding='utf-8') as file: # la r en 'r'
        respuestas = json.load(file)

    # creamos lista de respuesta segun la emoción detectada
    respuestas_generada = []

    for emocion in emociones_detectadas:
        if emocion in respuestas:
            respuesta = random.choice(respuestas[emocion])
            respuestas_generada.append(respuesta)

    # Si no se detectó ninguna emoción, devolver una respuesta por defecto
    if not respuestas_generada and "ninguna" in respuestas:
        respuestas_generada.append(random.choice(respuestas["ninguna"]))
    
    # retornamos la respuesta generada    
    return respuestas_generada