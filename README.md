# Proyecto Integrador - Gestor de Países (Programación 1)

Este proyecto es el trabajo integrador para la materia Programación 1. Es una aplicación de consola desarrollada en Python que permite gestionar, filtrar, ordenar y analizar información sobre países, leída desde un archivo CSV.

El sistema completo se ejecuta dentro de un contenedor de **Docker**, asegurando que funcione en cualquier máquina sin necesidad de instalar Python o librerías manualmente.

##  Desarrollo y Colaboración

Este proyecto fue desarrollado en equipo por

* **Valentín Tello** 
* **Santino Dalla Torre**

Utilizamos Git como sistema de control de versiones y GitHub Desktop para coordinar el trabajo. El flujo de trabajo incluyó la división de tareas (lógica de backend vs. interfaz de consola) y la resolución de conflictos para integrar nuestro código

##  Funcionalidades Principales

El programa presenta un menú interactivo de consola que permite:

* **Buscar un país** por nombre (con coincidencia parcial).
* **Filtrar países** por:
    * Continente.
    * Rango de población.
    * Rango de superficie.
* **Ordenar países** por:
    * Nombre (alfabéticamente).
    * Población (ascendente o descendente).
    * Superficie (ascendente o descendente).
* **Mostrar Estadísticas** clave:
    * País con mayor y menor población.
    * Promedio de población y superficie.
    * Cantidad total de países por continente.
* **Interfaz Mejorada:** Limpieza de consola automática y paginación de resultados utilizando OS, además de que la consola está decorada con la librería `rich` de Python para presentar los datos en tablas limpias, con colores y paneles.

## Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Contenerización:** Docker
* **Interfaz de Consola:** Librería `rich`
* **Control de Versiones:** Git y GitHub
* **Manejo de Datos:** Módulo `csv` de Python

## Instrucciones de uso
# Instalación:
**1: Clonar el repositorio**
**Git clone: https://github.com/santinodallatorre2501-bit/Trabajo-Integrador.git**
**cd Trabajo-integrador**

**2: Instalar dependencias:**
**Esto lee el archivo requirements.txt e instala rich y requests.**
**pip install -r requirements.txt**
**Ejecutar la aplicación y listo**

**Opción 2:  Ejecución con Docker**
**Si tenés Docker Desktop instalado y corriendo, podés construir y correr la aplicación en un **contenedor 100% aislado**

**1. Construir la Imagen de Docker (Asegurate de estar en la carpeta raíz del proyecto, donde**
 **está el Dockerfile)**
**docker build -t tpi-utn .**
**2. Correr el Contenedor Esto inicia la aplicación en modo interactivo (-it) y la borra al **terminar (--rm).**
**docker run -it --rm tpi-utn**

## Obtención de datos 

**los datos obtenidos para el archivo CSV fueron tomados desde una API contenedora**
**de datos sobre países, población y superficie**
**URL: https://api-paises-zilz.onrender.com/paises**

*Entrada (Filtrar por Superficie):*
1.  El usuario elige la opción 2 (Filtrar países) en el menú principal.
2.  Elige la opción 3 (Filtrar por rango de superficie).
3.  El sistema solicita una superficie mínima (ej: 1000000).
4.  El sistema solicita una superficie máxima (ej: 5000000).

*Salida (Resultado):*
El sistema limpia la consola y muestra una *tabla paginada* (de 10 en 10) con todos los países cuya superficie (en km²) está entre 1.000.000 y 5.000.000. Si no encuentra resultados, muestra un panel de error



LINK DEL VIDEO EXPLICATIVO: https://drive.google.com/file/d/15vIESUhHsq8kcJvSBEp_JpyHKG32edc1/view?usp=sharing