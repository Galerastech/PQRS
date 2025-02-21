import os

def crear_init_py(ruta_carpeta):
    """Crea un archivo __init__.py vacío en la carpeta especificada."""
    ruta_archivo = os.path.join(ruta_carpeta, '__init__.py')
    if not os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'w') as f:
            pass

def recorrer_carpetas(ruta_raiz):
    """Recorre las carpetas y subcarpetas a partir de la ruta raíz y crea archivos __init__.py."""
    for carpeta, subcarpetas, archivos in os.walk(ruta_raiz):
        print(f"Carpeta: {carpeta}")
        crear_init_py(carpeta)
        print("recorrido finalizado")


ruta_proyecto = "g:/EDISON/computador/VARIOS EDISON/PROHIBIDO NO TOCAR/CursoPrepHenry/Galeras_tech/PQRS/src/"  
recorrer_carpetas(ruta_proyecto)