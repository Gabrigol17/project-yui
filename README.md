## 📘 Proyecto: **Yui – IA de Apoyo Emocional en Mundo Virtual**

### 🎯 **Objetivo General**

Crear un juego interactivo tipo simulador con una IA emocional llamada **Yui**, inspirada en *Sword Art Online*, que:

* Acompaña emocionalmente al jugador.
* Aprende del usuario con el tiempo.
* Permite explorar un entorno virtual simple y registrar el progreso.

---

### 🧩 **Estructura del Proyecto**

#### 1. **IA – Yui (Apoyo emocional)**

* IA de tipo conversacional empática.
* Detecta emociones a partir del texto del jugador.
* Responde emocionalmente según la situación.
* Guarda historial de interacciones.
* Aprende patrones emocionales del jugador para mejorar futuras respuestas.

##### 🔧 Composición del módulo `yui.py`

* `analizar_emocion(texto_usuario)`: analiza la emoción (con IA externa o lógica simple).
* `responder_emocion(emocion, texto_usuario)`: genera una respuesta empática.
* `guardar_interaccion(usuario, texto, emocion, respuesta)`: registra cada interacción.
* `revisar_historial(usuario)`: revisa datos anteriores para personalizar futuras respuestas.

---

#### 2. **Exploración de mapa / Mundo virtual**

* Sistema básico de exploración por texto o nodos.
* Comportamientos simples por zona: eventos, ítems, climas, etc.
* Cambios en el estado emocional pueden influir en el entorno (ej: clima triste si el jugador está decaído).

---

#### 3. **Persistencia de datos / Guardado**

* Uso de **almacenamiento local** individual por usuario.
* Cada usuario tiene su propio archivo `datos.db` y carpeta de configuración.
* Guardado automático al salir de la app y cargado al iniciar.

### 🎯 **Expectativas del Proyecto**

* Que el jugador sienta a Yui como una compañera emocional real.
* Que el sistema se adapte poco a poco al jugador mediante historial.
* Que el mapa y las acciones del jugador estén conectadas emocionalmente con Yui.
* Que el proyecto sirva como base para futuras expansiones (interfaz visual, IA generativa, personajes secundarios, etc.)
