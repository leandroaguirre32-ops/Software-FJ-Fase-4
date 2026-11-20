
# Sistema Integral Software FJ

## 1. Descripción del proyecto

Software FJ es un sistema desarrollado en Python para gestionar clientes, servicios y reservas.

El sistema permite registrar clientes, administrar diferentes servicios, realizar reservas, calcular costos y controlar errores mediante excepciones personalizadas.

## 2. Objetivo

Desarrollar una aplicación organizada mediante programación orientada a objetos, aplicando abstracción, herencia, encapsulación y polimorfismo.

## 3. Tecnologías utilizadas

- Lenguaje de programación: Python.
- Entorno de desarrollo: Visual Studio Code.
- Control de versiones: Git.
- Repositorio: GitHub.

## 4. Estructura del proyecto

- main.py: programa principal.
- `entidades.py`: clases y gestión de clientes.
- `servicios.py`: servicios especializados.
- `reservas.py`: gestión de reservas.
- `excepciones.py`: manejo de errores.
- `logs.txt`: registro de eventos y errores.
- `.gitignore`: archivos excluidos del repositorio.

## 5. Servicios disponibles

- Reserva de salas.
- Alquiler de equipos.
- Asesorías especializadas.
- Validación de servicios no disponibles.

## 6. Ejecución del programa

Para ejecutar el sistema, se debe tener Python instalado.

Abrir la terminal en la carpeta del proyecto y ejecutar:

```bash
py main.py
```

## 7. Manejo de errores

Los métodos de cálculo aceptan parámetros opcionales para descuento e impuesto; el alquiler de equipos también admite la cantidad de unidades. Así se ofrecen distintas variantes de cálculo mediante la firma flexible de Python.

El sistema utiliza excepciones personalizadas para controlar datos incorrectos, servicios no disponibles y operaciones no permitidas.

También utiliza el módulo `logging` para registrar los eventos y errores en `logs.txt`.

## 8. Autor

Leandro Aguirre

Universidad Nacional Abierta y a Distancia (UNAD)

Fase 4 - Sistema Integral Software FJ

