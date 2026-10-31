```mermaid
graph TD
    subgraph Cliente
        HTML[Plantillas HTML / CSS]
    end
    
    subgraph Servidor Django
        URL[urls.py Enrutador] -->|Petición HTTP| VIEWS[views.py Vistas]
        VIEWS -->|Renderiza| HTML
        VIEWS -->|ORM Queries| MODELS[models.py Modelos]
    end
    
    subgraph Base de Datos
        MODELS -->|Lectura / Escritura| DB[(db.sqlite3)]
    end
    ```