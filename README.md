# Odoo Scale Connector

Este proyecto es un middleware local diseñado para conectar balanzas físicas (mediante puertos seriales/USB) con el cliente web de Odoo 19 Community. 

El servicio actúa como un puente de hardware a web: lee los datos crudos del puerto COM usando PySerial, los limpia y expone un endpoint local consumible directamente desde el frontend de Odoo (OWL o JavaScript) mediante peticiones HTTP.

## Arquitectura

- **Hardware:** Comunicación vía RS232/USB emulado como puerto COM.
- **Núcleo de lectura:** Python con la librería `pyserial`.
- **Servidor Web:** FastAPI corriendo sobre Uvicorn para servir los datos en tiempo real al navegador local.
- **Empaquetado:** PyInstaller para distribución como ejecutable independiente (.exe) en entornos Windows sin necesidad de instalar Python.

## Estructura del Proyecto

El código fuente principal se desarrolla bajo el entorno virtual. Las configuraciones locales (puertos, baudios) se manejan a través de variables de entorno para evitar recompilaciones durante la instalación en múltiples equipos físicos.

*(Las instrucciones de instalación, compilación y despliegue como servicio de Windows se documentarán conforme avance el desarrollo de los módulos core).*