# EcoEnergy - Proyecto Integrado (Back-End)

## Descripción y Objetivo
Este proyecto constituye el núcleo del desarrollo Back-End para la plataforma **EcoEnergy**, construido en Python utilizando el framework web Django. Su objetivo es proporcionar una arquitectura de software robusta, escalable y mantenible para gestionar los recursos y servicios energéticos del proyecto.

---

## Requisitos Previos

* **Python:** Versión `3.14.7` instalada en el sistema.
* **Git:** Para el control de versiones y clonación del repositorio.
* **Terminal Bash:** (Ejemplo: Git Bash en Windows / Zsh / Bash en Unix).

---

## Clonación del Repositorio

Para clonar el repositorio localmente, ejecuta el siguiente comando en tu terminal:

```bash
git clone <URL_DEL_REPOSITORIO>
cd django-p2c1-CortesAlexander

## Documentación de Templates, Views y Navegación

### Estructura de Plantillas
* **Plantilla base:** `templates/base.html`
* **Plantillas de la aplicación:**
  * `templates/dispositivos/inicio.html`
  * `templates/dispositivos/catalogo.html`
  * `templates/dispositivos/numero_dispositivo.html`

### Rutas Funcionales y Datos de Contexto (Views)

| Ruta (URL) | Vista (`View`) | Claves de Contexto | Descripción / Datos Preparados |
| :--- | :--- | :--- | :--- |
| `/` | `inicio` | `sistema`, `mensaje`, `asignatura` | Retorna la vista principal con información de la asignatura y el sistema EcoEnergy. |
| `/dispositivos/` | `catalogo` | `dispositivos` | Prepara una lista de diccionarios con dispositivos ("Medidor inteligente", "Sensor de temperatura", "Climatizador") y sus estados. |
| `/dispositivos/<int:dispositivo_id>/` | `dispositivo_numero` | `dispositivo_id`, `dispositivos` | Valida que la ID sea 2 (de lo contrario retorna 404). Si es correcta, genera y entrega una lista detallada de dispositivos. |
| `/zonas/<int:zona_id>/dispositivos/` | `dispositivos_zona` | *N/A (Respuesta Directa)* | Valida que la ID de zona sea 3 (de lo contrario retorna 404). Devuelve un `HttpResponse` plano con el texto de la zona. |

### Ejecución y Prueba de Navegación

1. **Iniciar el servidor local:**
   ```bash
   python manage.py runserver