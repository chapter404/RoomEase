1 - Ejecutar el script 'bd_roomease_mysql.sql' con MySQL para crear la base de datos y las tablas [Las credenciales (user y pass) del servidor mysq deben ser ambas "root"]
2 - Desde la terminal ir a la carpeta del backend y crear el entorno virtual de python con el comando -> python -m venv venv
3 - Activar el entorno virtual con el comando -> .\venv\Scripts\activate (para desactivar el entorno virtual ejecutar el comando -> deactivate)
4 - Instalar las dependencias para ejecutar el backend con el comando -> pip install -r requirements.txt
5 - Ir a la carpeta src del backend y ejecutar el servidor local con el comando -> uvicorn main:app --reload --host 127.0.0.1 --port 8000
6 - Ir a la carpeta src del frontend y ejecutar el servidor local con el comando -> ng serve
7 - Abrir la pagina web en el navegador con la url -> localhost:4200/login