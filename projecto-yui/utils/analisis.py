import re
from yui.emociones import estado_animo

def analizar_emocion(texto_usuario):
    texto_usuario = texto_usuario.lower()  # Normalizar a minúsculas
    palabras_usuario = re.findall(r'\b\w+\b', texto_usuario)  # Separar por palabras usando expresiones regulares

    conteo_emociones = {}  # Diccionario para contar coincidencias por emoción

    for emocion, palabras_clave in estado_animo.items():
        for palabra in palabras_clave:
            if palabra in palabras_usuario: 
                # Si la palabra está en el texto, sumar al conteo de esa emoción
                if emocion in conteo_emociones:
                    conteo_emociones[emocion] += 1
                else:
                    conteo_emociones[emocion] = 1

    # Si no se detectó ninguna emoción, devolver 'ninguna'
    if not conteo_emociones:
        return ["ninguna"]

    # Obtener el mayor conteo
    max_conteo = max(conteo_emociones.values())

    # Devolver todas las emociones que tengan ese máximo conteo
    emociones_detectadas = [emocion for emocion, conteo in conteo_emociones.items() if conteo == max_conteo]

    return emociones_detectadas
