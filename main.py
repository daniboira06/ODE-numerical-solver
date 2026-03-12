import numpy as np
import matplotlib.pyplot as plt
from odes import (oscilador_armonico, oscilador_armonico_analitica,
                  pendulo, pendulo_analitica,
                  lorenz, lotka_volterra)
from solvers import euler, rk4, rk45
from plots import (plot_solucion, plot_error, plot_fase,
                   plot_lorenz, plot_lotka_volterra, animate_oscilador)

# ── Menú principal ────────────────────────────────────────────────
print("\n╔══════════════════════════════════════╗")
print("║       ODE NUMERICAL SOLVER           ║")
print("╠══════════════════════════════════════╣")
print("║  1. Oscilador armónico               ║")
print("║  2. Péndulo simple                   ║")
print("║  3. Sistema de Lorenz                ║")
print("║  4. Lotka-Volterra                   ║")
print("╚══════════════════════════════════════╝")
caso = input("\nElige un caso (1-4): ").strip()

print("\nElige el integrador:")
print("  1. Euler")
print("  2. RK4")
print("  3. RK45 adaptativo")
integ = input("Integrador (1-3): ").strip()

# ── Parámetros comunes ────────────────────────────────────────────
dt  = float(input("Paso de tiempo dt (recomendado 0.01): ") or "0.01")
N   = int(input("Número de pasos N (recomendado 1000): ") or "1000")
t0  = 0.0

integradores_fijos = {"1": euler, "2": rk4}
usar_rk45 = integ == "3"

# ── Caso 1: Oscilador armónico ────────────────────────────────────
if caso == "1":
    omega = float(input("Frecuencia omega (recomendado 1.0): ") or "1.0")
    x0    = float(input("Posición inicial x0 (recomendado 1.0): ") or "1.0")
    v0    = float(input("Velocidad inicial v0 (recomendado 0.0): ") or "0.0")
    y0    = np.array([x0, v0])
    f     = lambda t, y: oscilador_armonico(t, y, omega=omega)

    if usar_rk45:
        t_arr, y_arr = rk45(f, t0, y0, t_end=t0 + N*dt)
    else:
        solver = integradores_fijos.get(integ, rk4)
        t_arr, y_arr = solver(f, t0, y0, dt, N)

    y_ana = oscilador_armonico_analitica(t_arr, x0, v0, omega)
    nombre = f"Oscilador Armónico - {['Euler','RK4','RK45'][int(integ)-1]}"

    plot_solucion(t_arr, y_arr, y_ana, labels=["x", "v"], title=nombre)
    plot_error(t_arr, y_arr, y_ana, title=f"Error - {nombre}")
    plot_fase(y_arr, labels=("x", "v"), title=f"Fase - {nombre}")
    ani = animate_oscilador(t_arr, y_arr, title=nombre)

# ── Caso 2: Péndulo ───────────────────────────────────────────────
elif caso == "2":
    g      = float(input("Gravedad g (recomendado 9.8): ") or "9.8")
    L      = float(input("Longitud L (recomendado 1.0): ") or "1.0")
    theta0 = float(input("Ángulo inicial en grados (recomendado 10): ") or "10")
    theta0 = np.radians(theta0)
    y0     = np.array([theta0, 0.0])
    f      = lambda t, y: pendulo(t, y, g=g, L=L)

    if usar_rk45:
        t_arr, y_arr = rk45(f, t0, y0, t_end=t0 + N*dt)
    else:
        solver = integradores_fijos.get(integ, rk4)
        t_arr, y_arr = solver(f, t0, y0, dt, N)

    y_ana = pendulo_analitica(t_arr, theta0, g=g, L=L)
    nombre = f"Péndulo - {['Euler','RK4','RK45'][int(integ)-1]}"

    plot_solucion(t_arr, y_arr, y_ana, labels=["θ", "ω"], title=nombre)
    plot_error(t_arr, y_arr, y_ana, title=f"Error - {nombre}")
    plot_fase(y_arr, labels=("θ", "ω"), title=f"Fase - {nombre}")

# ── Caso 3: Lorenz ────────────────────────────────────────────────
elif caso == "3":
    print("Parámetros de Lorenz (Enter para valores clásicos):")
    sigma = float(input("  sigma (10.0): ") or "10.0")
    rho   = float(input("  rho   (28.0): ") or "28.0")
    beta  = float(input("  beta  (2.667): ") or "2.6667")
    y0    = np.array([1.0, 1.0, 1.0])
    f     = lambda t, y: lorenz(t, y, sigma=sigma, rho=rho, beta=beta)

    if usar_rk45:
        t_arr, y_arr = rk45(f, t0, y0, t_end=t0 + N*dt)
    else:
        solver = integradores_fijos.get(integ, rk4)
        t_arr, y_arr = solver(f, t0, y0, dt, N)

    nombre = f"Lorenz - {['Euler','RK4','RK45'][int(integ)-1]}"
    plot_lorenz(y_arr, title=nombre)
    plot_solucion(t_arr, y_arr, labels=["x", "y", "z"], title=nombre)

# ── Caso 4: Lotka-Volterra ────────────────────────────────────────
elif caso == "4":
    print("Parámetros de Lotka-Volterra (Enter para valores por defecto):")
    alpha = float(input("  alpha (1.0):  ") or "1.0")
    beta  = float(input("  beta  (0.1):  ") or "0.1")
    delta = float(input("  delta (0.075):") or "0.075")
    gamma = float(input("  gamma (1.5):  ") or "1.5")
    x0    = float(input("Población inicial presas (40): ") or "40")
    p0    = float(input("Población inicial depredadores (9): ") or "9")
    y0    = np.array([x0, p0])
    f     = lambda t, y: lotka_volterra(t, y, alpha=alpha, beta=beta,
                                         delta=delta, gamma=gamma)

    if usar_rk45:
        t_arr, y_arr = rk45(f, t0, y0, t_end=t0 + N*dt)
    else:
        solver = integradores_fijos.get(integ, rk4)
        t_arr, y_arr = solver(f, t0, y0, dt, N)

    nombre = f"Lotka-Volterra - {['Euler','RK4','RK45'][int(integ)-1]}"
    plot_lotka_volterra(t_arr, y_arr, title=nombre)

else:
    print("Opción no válida.")
    exit()

plt.show()