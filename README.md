# RoomEase

## Instrucciones para ejecutar el sistema en modo local

1. **Ejecutar el script `bd_roomease_mysql.sql`** con MySQL para crear la base de datos y las tablas.
   - **Credenciales**: El servidor MySQL debe tener las credenciales:
     - Usuario: `root`
     - Contraseña: `root`

2. **Crear el entorno virtual de Python**:
   - Desde la terminal, ve a la carpeta del backend y ejecuta el siguiente comando:
     ```bash
     python -m venv venv
     ```

3. **Activar el entorno virtual**:
   - En sistemas Windows, usa:
     ```bash
     .\venv\Scripts\activate
     ```
   - Para desactivar el entorno virtual, ejecuta:
     ```bash
     deactivate
     ```

4. **Instalar las dependencias del backend**:
   - En la carpeta del backend, ejecuta:
     ```bash
     pip install -r requirements.txt
     ```

5. **Ejecutar el servidor backend local**:
   - En la carpeta `src` del backend, ejecuta:
     ```bash
     uvicorn main:app --reload --host 127.0.0.1 --port 8000
     ```

7. **Ejecutar el servidor frontend local**:
   - En la carpeta frontend, ejecuta:
     ```bash
     ng serve
     ```

8. **Instalar Angular en el frontend (solo la primera vez)**:
   - En la carpeta frontend, ejecuta:
     ```bash
     ng serve
     ```

9. **Abrir la página web en el navegador**:
   - Dirígete a la siguiente URL en tu navegador:
     ```
     http://localhost:4200/login
     ```
