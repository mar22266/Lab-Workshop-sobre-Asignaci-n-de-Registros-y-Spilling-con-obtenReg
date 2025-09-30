# Construcción de Compiladores — obtenReg

**Resumen:**  
Este laboratorio implementa y demuestra obtenReg, un asignador de registros que decide cuándo reutilizar registros y cuándo hacer _spilling_ (derramar a memoria) al agotarse los registros; incluye ejemplos guiados sin/con _spilling_, una reescritura eficiente de TAC usando solo 3 registros (R1–R3) y la traducción de un bloque Java a código máquina respetando vida útil de variables. Se provee una implementación en Python con política simple (FIFO).

---

## ¿Qué hace el programa?

- Asigna registros (R1, R2, R3) a variables, reutilizando si ya están cargadas.
- Derrama a memoria (_spilling_) cuando no hay registros libres (política simple FIFO).
- Muestra el estado de registros y memoria después de las asignaciones.

---

## Estructura

- `code/alloc_simple.py` — Asignador de registros.
- `code/alloc_next_use.py` — Asignador con _next-use_.
- `code/tests.py` — Pruebas demuestra asignaciones y un derrame.

---

## Cómo ejecutar

```bash
python code/tests.py
```
