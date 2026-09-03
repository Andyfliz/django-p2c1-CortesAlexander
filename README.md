# EcoEnergy - Proyecto Integrado (Back-End)

## Descripción y Objetivo

Este proyecto constituye el desarrollo Back-End de la plataforma **EcoEnergy**, construido en **Python** utilizando el framework web **Django**.

Su objetivo es proporcionar una arquitectura de software organizada, mantenible y escalable para gestionar los recursos y servicios energéticos del proyecto, utilizando el patrón **MVT (Model-View-Template)** y la separación de responsabilidades.

---

## Requisitos Previos

Antes de ejecutar el proyecto, se requiere tener instalado:

* **Python:** versión `3.14.7`
* **Git:** para clonar el repositorio y gestionar el control de versiones.
* **Terminal Bash:** por ejemplo, Git Bash en Windows, Bash o Zsh en sistemas Unix.

---

## Instalación y Configuración

### 1. Clonar el repositorio

Desde una terminal Bash, clonar el repositorio y acceder a la carpeta del proyecto:

```bash
git clone <URL_DEL_REPOSITORIO>
cd django-p2c1-CortesAlexander
```

### 2. Crear el entorno virtual

Crear un entorno virtual para mantener aisladas las dependencias del proyecto:

```bash
python -m venv .venv
```

### 3. Activar el entorno virtual

En Git Bash:

```bash
source .venv/Scripts/activate
```

Una vez activado, la terminal debería mostrar `(.venv)` al inicio de la línea.

### 4. Instalar las dependencias

Actualizar `pip` e instalar las dependencias indicadas en `requirements.txt`:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Verificar las dependencias

Comprobar que no existan conflictos entre los paquetes instalados:

```bash
python -m pip check
```

### 6. Validar la configuración de Django

Ejecutar la comprobación de Django para verificar que el proyecto esté correctamente configurado:

```bash
python manage.py check
```

### 7. Iniciar el servidor

Para ejecutar el proyecto localmente:

```bash
python manage.py runserver
```

Luego, acceder desde el navegador a la dirección indicada por Django.

---

## Control de Versiones con Git

Una vez realizados cambios en el proyecto, se deben guardar y registrar utilizando Git.

### 1. Guardar los cambios

Guardar los archivos modificados desde el editor utilizando:

```text
Ctrl + S
```

Esto guarda los cambios en el computador, pero todavía no los registra en el historial de Git.

### 2. Revisar el estado del repositorio

Antes de registrar los cambios, es recomendable verificar qué archivos fueron modificados:

```bash
git status
```

### 3. Preparar los cambios

Para agregar el archivo `README.md`:

```bash
git add README.md
```

También se pueden agregar todos los archivos modificados:

```bash
git add .
```

### 4. Crear el commit

Registrar los cambios en el historial de Git:

```bash
git commit -m "docs: actualizar README con pasos de instalación y documentación MVT"
```

El `commit` funciona como un punto de control del proyecto y permite identificar exactamente qué cambios fueron registrados.

### 5. Subir los cambios a GitHub

Enviar los commits al repositorio remoto:

```bash
git push origin main
```

De esta manera, los cambios realizados localmente quedan disponibles en el repositorio remoto.

---

## Estado del Proyecto

Actualmente, el proyecto cuenta con la configuración inicial del entorno de desarrollo y la estructura Back-End basada en Django.

Se continúa trabajando en la implementación de las funcionalidades correspondientes al proyecto **EcoEnergy**, incluyendo la gestión y visualización de zonas y dispositivos energéticos.

---

## Tecnologías Utilizadas

* Python
* Django
* Git
* GitHub
* HTML
* Bootstrap
* Archivos JSON como fuente de datos
