# VRPTW Optimization using Local Search Heuristics

## Descripción del Proyecto

Este proyecto aborda el Problema de Ruteo de Vehículos con Ventanas de Tiempo (VRPTW), que consiste en planificar rutas óptimas para una flota de vehículos que deben realizar entregas a múltiples clientes, cada uno con una ventana de tiempo específica. El objetivo es minimizar los costos operativos, como la distancia total recorrida, mientras se cumple con las restricciones de tiempo y capacidad de los vehículos.

## Objetivos

### Objetivo General
Desarrollar una solución óptima para el VRPTW mediante la aplicación de la heurística de búsqueda local (Local Search).

### Objetivos Específicos
1. Analizar las características clave del VRPTW para obtener una comprensión profunda del mismo.
2. Desarrollar e implementar un algoritmo adaptado para abordar el VRPTW.
3. Realizar pruebas para evaluar el rendimiento y la eficacia del algoritmo propuesto.

## Metodología

### Planteamiento del Problema
El VRPTW es una extensión del problema de enrutamiento de vehículos (VRP) que incluye ventanas de tiempo específicas para cada cliente. Los vehículos deben atender a los clientes dentro de estas ventanas de tiempo, respetando las capacidades de carga y minimizando los costos operativos.

### Herramientas Utilizadas
- **Lenguaje de Programación:** Python
- **Hardware:** PC con CPU AMD Ryzen 5 2500u, GPU Rx 560x, 16GB RAM

### Algoritmo Implementado
Se desarrolló una heurística de búsqueda local para abordar el VRPTW, optimizando las rutas de los vehículos para minimizar la distancia total recorrida y cumplir con las ventanas de tiempo asignadas.

### Resultados
El algoritmo desarrollado genera rutas optimizadas que se visualizan mediante gráficos, mostrando las rutas de los vehículos y los tiempos de entrega para cada cliente.

## Archivos

- `heuristicas.py`: Contiene la implementación del algoritmo de búsqueda local.
- `c101.sol`: Archivo de solución que muestra las rutas optimizadas.
- `c101.png`: Grafico de la solucion.

## Ejecución del Proyecto

1. Clona este repositorio: 
    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd tu_repositorio
    ```
3. Ejecuta el script principal:
    ```bash
    python main.py
    ```

## Conclusión

El proyecto demuestra cómo la heurística de búsqueda local puede ser una herramienta eficaz para abordar problemas complejos de optimización combinatoria como el VRPTW. A través del análisis, desarrollo e implementación del algoritmo, se logró mejorar la eficiencia y reducir los costos operativos en la planificación de rutas de vehículos.

## Contacto

Para más información, puedes contactarme en [tu_email@dominio.com].

---

Este README proporciona una visión general clara y concisa de tu proyecto, sus objetivos, la metodología utilizada y cómo ejecutar el código, facilitando a otros usuarios entender y replicar tu trabajo.

Referencias
https://github.com/donfaq/VRPTW/blob/master/draw_solution.ipynb
