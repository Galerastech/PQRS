# PQRS

<div align="center">
  <img src="https://github.com/Galerastech/PQRS/blob/develop/assets/icons/icon_web.jpeg?raw=true" alt="Logo del proyecto" style="width:200px; border-radius: 100%;">
</div>

## Inicialización del Proyecto

1. Clonar el repositorio usando:

    ```bash
    git clone https://github.com/Galerastech/PQRS.git
    ```

2. Accedemos al repositorio:

    ```bash
    cd PQRS
    ```

3. Crear y activar el entorno virtual:

    - En Windows:
      ```bash
      python -m venv .venv
      .venv\Scripts\activate
      ```
    - En macOS/Linux:
      ```bash
      python3 -m venv .venv
      source .venv/bin/activate
      ```

4. Instalar las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Arrancar la API

1. Modificar el archivo `.env.example` a `.env` y agregar las configuraciones correspondientes para la base de datos. Asegúrate de que la base de datos tenga el mismo nombre que se usa en el archivo `.env`.
   
2. Aplicar migraciones:

    ```bash
    alembic upgrade head
    ```

3. Arrancar FastAPI **(se iniciará en el puerto 8001)**:

    ```bash
    uvicorn backend.backend:app --reload --port 8001
    ```

   Usando la bandera `--port`, puedes definir el puerto donde inicializará la API.

   > 💡 **Tip:** Para la documentación de la API, usa la ruta `http://localhost:8001/docs`.

## Arrancar la Aplicación en Flet

1. Usar el siguiente comando para correr la aplicación:

    ```bash
    flet run -r
    ```

   > 💡 **Tip:** Asegúrate de tener Flet instalado correctamente antes de ejecutar este comando. Si no está instalado, usa `pip install flet` para instalarlo.
entes entornos como [**Entonrnos**](https://flet.dev/docs/reference/cli/run)
