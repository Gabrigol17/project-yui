import re
from yui.emociones import estado_animo
import difflib

def analizar_emocion(texto_usuario):
    texto_usuario = texto_usuario.lower()  # Normalizar a minúsculas
    palabras_usuario = re.findall(r'\b\w+\b', texto_usuario)  # Separar por palabras usando expresiones regulares

    conteo_emociones = {}  # Diccionario para contar coincidencias por emoción
    umbral_similitud = 0.7  # Umbral de similitud para considerar una coincidencia

    for emocion, palabras_clave in estado_animo.items():
        for palabra_clave in palabras_clave:
            for palabra_usuario in palabras_usuario:
                similitud = difflib.SequenceMatcher(None, palabra_clave, palabra_usuario).ratio()
                print(f"Comparando '{palabra_clave}' con '{palabra_usuario}': similitud = {similitud:.2f}")  # Debugging
                if similitud >= umbral_similitud:  # Verificar similitud con un umbral
                    print(f"Emoción detectada: {emocion} por la palabra '{palabra_usuario}'")
                    if emocion in conteo_emociones:
                        conteo_emociones[emocion] += 1
                    else:
                        conteo_emociones[emocion] = 1
                    break  # Evita contar la misma palabra clave varias veces por emoción

    # Si no se detectó ninguna emoción, devolver 'ninguna'
    if not conteo_emociones:
        return ["ninguna"]

    # Obtener el mayor conteo
    max_conteo = max(conteo_emociones.values())

    # Devolver todas las emociones que tengan ese máximo conteo
    emociones_detectadas = [emocion for emocion, conteo in conteo_emociones.items() 
                            if conteo == max_conteo]

    return emociones_detectadas
