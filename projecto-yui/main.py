from utils.db import listar_usuarios, crear_bd_usuario

crear_bd_usuario("Gabriel")
listar_usuarios()

usuario = listar_usuarios()
print(f"usuarios encontrados:", usuario)
