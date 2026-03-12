import numpy as np

# ── Oscilador armónico ────────────────────────────────────────────
# x'' + w²x = 0  →  sistema: x' = v, v' = -w²x
def oscilador_armonico(t, y, omega=1.0):
    """
    y = [x, v]
    Solución analítica: x(t) = x0*cos(wt) + (v0/w)*sin(wt)
    """
    x, v = y
    return np.array([v, -omega**2 * x])

def oscilador_armonico_analitica(t, x0, v0, omega=1.0):
    return x0 * np.cos(omega * t) + (v0 / omega) * np.sin(omega * t)

# ── Péndulo simple ────────────────────────────────────────────────
# θ'' + (g/L)sin(θ) = 0  →  sistema: θ' = w, w' = -(g/L)sin(θ)
def pendulo(t, y, g=9.8, L=1.0):
    """
    y = [theta, omega]
    Para ángulos pequeños: solución analítica = oscilador armónico
    """
    theta, omega = y
    return np.array([omega, -(g / L) * np.sin(theta)])

def pendulo_analitica(t, theta0, omega0=0.0, g=9.8, L=1.0):
    # Aproximación ángulos pequeños
    w = np.sqrt(g / L)
    return theta0 * np.cos(w * t) + (omega0 / w) * np.sin(w * t)

# ── Sistema de Lorenz ─────────────────────────────────────────────
# dx/dt = sigma*(y-x)
# dy/dt = x*(rho-z) - y
# dz/dt = x*y - beta*z
def lorenz(t, y, sigma=10.0, rho=28.0, beta=8/3):
    """
    y = [x, y, z]
    Parámetros clásicos: sigma=10, rho=28, beta=8/3
    """
    x, y_, z = y
    dx = sigma * (y_ - x)
    dy = x * (rho - z) - y_
    dz = x * y_ - beta * z
    return np.array([dx, dy, dz])

# ── Lotka-Volterra ────────────────────────────────────────────────
# dx/dt = alpha*x - beta*x*y   (presas)
# dy/dt = delta*x*y - gamma*y  (depredadores)
def lotka_volterra(t, y, alpha=1.0, beta=0.1, delta=0.075, gamma=1.5):
    """
    y = [x, y] -> [presas, depredadores]
    """
    x, pred = y
    dx   = alpha * x - beta * x * pred
    dpred = delta * x * pred - gamma * pred
    return np.array([dx, dpred])