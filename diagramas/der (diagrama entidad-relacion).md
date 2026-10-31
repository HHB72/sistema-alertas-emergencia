erDiagram
    USER {
        int id PK
        string username
        string password
        boolean is_staff
        boolean is_superuser
    }
    GUIA_PRIMEROS_AUXILIOS {
        int id PK
        string titulo
        text contenido
    }
    CONTACTO_EMERGENCIA {
        int id PK
        string nombre
        string telefono
    }
    INCIDENTE {
        int id PK
        string tipo
        string afectados
        text descripcion
        datetime fecha_creacion
    }