```mermaid
graph TD
    User([Usuario / Ciudadano]) -->|Interactúa vía Web| System[Sistema de Emergencias Django]
    Admin([Administrador]) -->|Gestiona Contenido| System
    System -->|Almacena y Recupera| DB[(Base de Datos SQLite)]
    ```