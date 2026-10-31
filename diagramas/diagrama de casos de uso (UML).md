```mermaid
graph LR
    subgraph Sistema de Emergencias
        UC1[Iniciar Sesión / Registrarse]
        UC2[Activar Botón SOS]
        UC3[Consultar Primeros Auxilios]
        UC4[Registrar Incidente]
        UC5[Gestionar Contactos de Emergencia]
        UC6[Ver Hospitales Cercanos]
        UC7[Acceder al Panel de Administración]
    end
    
    User([Usuario / Ciudadano]) --> UC1
    User --> UC2
    User --> UC3
    User --> UC4
    User --> UC5
    User --> UC6
    
    Admin([Administrador]) --> UC1
    Admin --> UC7
    ```