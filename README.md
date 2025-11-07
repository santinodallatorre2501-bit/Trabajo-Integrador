# 🌍 Proyecto Integrador - Gestor de Países (Programación 1)

Este proyecto es el trabajo integrador para la materia Programación 1. Es una aplicación de consola desarrollada en Python que permite gestionar, filtrar, ordenar y analizar información sobre países, leída desde un archivo CSV.

El sistema completo se ejecuta dentro de un contenedor de **Docker**, asegurando que funcione en cualquier máquina sin necesidad de instalar Python o librerías manualmente.

## 👥 Desarrollo y Colaboración

Este proyecto fue desarrollado en equipo por:

* **Valentín Tello** 
* **Santino Dalla Torre**

Utilizamos **Git** como sistema de control de versiones y **GitHub Desktop** para coordinar el trabajo. El flujo de trabajo incluyó la división de tareas (lógica de backend vs. interfaz de consola) y la resolución de conflictos para integrar nuestro código.

## ✨ Funcionalidades Principales

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
* **Interfaz Mejorada:** La consola está decorada con la librería `rich` de Python para presentar los datos en tablas limpias, con colores y paneles.

## Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Contenerización:** Docker
* **Interfaz de Consola:** Librería `rich`
* **Control de Versiones:** Git y GitHub
* **Manejo de Datos:** Módulo `csv` de Python

---

