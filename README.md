# ODE Numerical Solver 📐

Resolución numérica de ecuaciones diferenciales ordinarias (ODEs) de interés físico, con comparación respecto a soluciones analíticas.

## Descripción

Este proyecto implementa tres métodos de integración numérica para resolver ODEs y los aplica a cuatro sistemas físicos clásicos. Permite comparar la precisión de cada método y visualizar las soluciones.

## Estructura del proyecto
```
ODE-solver/
├── main.py        # Script principal con menú interactivo
├── odes.py        # Definición de las ecuaciones diferenciales
├── solvers.py     # Métodos de integración numérica
├── plots.py       # Gráficos y animaciones
├── requirements.txt
├── examples/
│   └── demo.ipynb
└── README.md
```

## Instalación
```bash
pip install -r requirements.txt
```

## Uso
```bash
python3 main.py
```

El programa te guiará por un menú interactivo:
```
╔══════════════════════════════════════╗
║       ODE NUMERICAL SOLVER           ║
╠══════════════════════════════════════╣
║  1. Oscilador armónico               ║
║  2. Péndulo simple                   ║
║  3. Sistema de Lorenz                ║
║  4. Lotka-Volterra                   ║
╚══════════════════════════════════════╝
```

## Sistemas implementados

**1. Oscilador armónico**
Sistema masa-resorte. Tiene solución analítica exacta, ideal para comparar precisión de integradores.

**2. Péndulo simple**
Oscilador no lineal. La solución analítica es válida solo para ángulos pequeños, lo que permite ver cuándo la aproximación lineal falla.

**3. Sistema de Lorenz**
Modelo de convección atmosférica. Ejemplo clásico de caos determinista y efecto mariposa. Genera el famoso atractor de Lorenz en 3D.

**4. Lotka-Volterra**
Dinámica de poblaciones depredador-presa. Las poblaciones oscilan de forma acoplada formando ciclos cerrados en el espacio de fases.

## Métodos de integración

| Método | Orden | Paso adaptativo | Precisión |
|--------|-------|----------------|-----------|
| Euler  | 1     | No             | Baja      |
| RK4    | 4     | No             | Alta      |
| RK45   | 4-5   | Sí             | Muy alta  |

## Gráficos generados

- Solución numérica vs analítica
- Error absoluto respecto a solución exacta
- Espacio de fases
- Atractor de Lorenz en 3D
- Animación del oscilador