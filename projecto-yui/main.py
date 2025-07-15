from yui.yui import generar_respuesta
import json
import random
import os
import time

os.system('cls' if os.name == 'nt' else 'clear')

# Ruta del archivo JSON
ruta_json = os.path.join(os.path.dirname(__file__), 'yui', 'respuesta.json')

# Mostrar un saludo al iniciar
with open(ruta_json, 'r', encoding='utf-8') as file:
    respuestas = json.load(file)
    if "saludo" in respuestas:
        print("Yui:", random.choice(respuestas["saludo"]))
        print("")
        time.sleep(1)
print("Bienvenido a Yui, tu asistente virtual. Escribe 'salir' para terminar la conversación.")
print("")
# Bucle principal
while True:
    texto_usuario = input("Tú: ").strip().lower()
    if texto_usuario == 'salir':
        if "despedida" in respuestas:
            print("Yui:", random.choice(respuestas["despedida"]))
        else:
            print("Yui: Hasta luego 💛")
        break

    respuesta = generar_respuesta(texto_usuario)
    print("Yui:", " ".join(respuesta))
    time.sleep(1)  
