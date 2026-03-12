import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ── Solución numérica vs analítica ────────────────────────────────
def plot_solucion(t, y_num, y_analitica=None, labels=None, title="Solución"):
    plt.figure(figsize=(10, 4))
    if labels is None:
        labels = [f"y[{i}]" for i in range(y_num.shape[1])]
    for i in range(y_num.shape[1]):
        plt.plot(t, y_num[:, i], label=f"Numérica - {labels[i]}")
    if y_analitica is not None:
        plt.plot(t, y_analitica, "--", color="red", label="Analítica")
    plt.xlabel("t")
    plt.title(title)
    plt.legend()
    plt.grid(True)

# ── Error respecto a solución analítica ───────────────────────────
def plot_error(t, y_num, y_analitica, title="Error"):
    error = np.abs(y_num[:, 0] - y_analitica)
    plt.figure(figsize=(10, 3))
    plt.semilogy(t, error, color="red")
    plt.xlabel("t")
    plt.ylabel("Error absoluto")
    plt.title(title)
    plt.grid(True)

# ── Espacio de fases ──────────────────────────────────────────────
def plot_fase(y_num, labels=("x", "v"), title="Espacio de fases"):
    plt.figure(figsize=(5, 5))
    plt.plot(y_num[:, 0], y_num[:, 1], color="blue")
    plt.scatter(y_num[0, 0], y_num[0, 1], color="green", zorder=5, label="Inicio")
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.axis("equal")

# ── Atractor de Lorenz (3D) ───────────────────────────────────────
def plot_lorenz(y_num, title="Atractor de Lorenz"):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(y_num[:, 0], y_num[:, 1], y_num[:, 2],
            lw=0.5, color="blue", alpha=0.8)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title(title)

# ── Lotka-Volterra ────────────────────────────────────────────────
def plot_lotka_volterra(t, y_num, title="Lotka-Volterra"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

    # Poblaciones en el tiempo
    ax1.plot(t, y_num[:, 0], label="Presas",       color="green")
    ax1.plot(t, y_num[:, 1], label="Depredadores", color="red")
    ax1.set_xlabel("t")
    ax1.set_ylabel("Población")
    ax1.set_title(f"{title} - Poblaciones")
    ax1.legend()
    ax1.grid(True)

    # Espacio de fases
    ax2.plot(y_num[:, 0], y_num[:, 1], color="purple")
    ax2.scatter(y_num[0, 0], y_num[0, 1], color="green", zorder=5, label="Inicio")
    ax2.set_xlabel("Presas")
    ax2.set_ylabel("Depredadores")
    ax2.set_title(f"{title} - Espacio de fases")
    ax2.legend()
    ax2.grid(True)

# ── Animación oscilador ───────────────────────────────────────────
def animate_oscilador(t, y_num, title="Oscilador"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Panel izquierdo: posición en el tiempo
    ax1.set_xlim(t[0], t[-1])
    ax1.set_ylim(y_num[:, 0].min() - 0.5, y_num[:, 0].max() + 0.5)
    ax1.set_xlabel("t")
    ax1.set_ylabel("x")
    ax1.set_title("Posición")
    ax1.grid(True)
    line1, = ax1.plot([], [], color="blue")
    punto1, = ax1.plot([], [], "o", color="blue")

    # Panel derecho: espacio de fases
    ax2.set_xlim(y_num[:, 0].min() - 0.5, y_num[:, 0].max() + 0.5)
    ax2.set_ylim(y_num[:, 1].min() - 0.5, y_num[:, 1].max() + 0.5)
    ax2.set_xlabel("x")
    ax2.set_ylabel("v")
    ax2.set_title("Espacio de fases")
    ax2.grid(True)
    line2, = ax2.plot([], [], color="orange")
    punto2, = ax2.plot([], [], "o", color="orange")

    fig.suptitle(title)

    def update(frame):
        line1.set_data(t[:frame], y_num[:frame, 0])
        punto1.set_data([t[frame]], [y_num[frame, 0]])
        line2.set_data(y_num[:frame, 0], y_num[:frame, 1])
        punto2.set_data([y_num[frame, 0]], [y_num[frame, 1]])
        return line1, punto1, line2, punto2

    ani = FuncAnimation(fig, update, frames=len(t), interval=20, blit=True)
    return ani