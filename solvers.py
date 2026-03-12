import numpy as np

# ── Euler ─────────────────────────────────────────────────────────
def euler(f, t0, y0, dt, N):
    """
    Integrador de Euler para ODEs.
    f  : función f(t, y)
    t0 : tiempo inicial
    y0 : condición inicial
    dt : paso de tiempo
    N  : número de pasos
    """
    t = t0
    y = y0.copy()
    t_list = [t]
    y_list = [y.copy()]

    for _ in range(N):
        y = y + dt * f(t, y)
        t = t + dt
        t_list.append(t)
        y_list.append(y.copy())

    return np.array(t_list), np.array(y_list)

# ── RK4 ───────────────────────────────────────────────────────────
def rk4(f, t0, y0, dt, N):
    """
    Integrador RK4 para ODEs.
    """
    t = t0
    y = y0.copy()
    t_list = [t]
    y_list = [y.copy()]

    for _ in range(N):
        k1 = f(t,            y)
        k2 = f(t + dt/2,     y + dt/2 * k1)
        k3 = f(t + dt/2,     y + dt/2 * k2)
        k4 = f(t + dt,       y + dt   * k3)
        y  = y + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)
        t  = t + dt
        t_list.append(t)
        y_list.append(y.copy())

    return np.array(t_list), np.array(y_list)

# ── RK45 adaptativo ───────────────────────────────────────────────
def rk45(f, t0, y0, t_end, tol=1e-6, dt_min=1e-6, dt_max=0.1):
    """
    Integrador RK45 adaptativo (Dormand-Prince).
    Ajusta el paso de tiempo automáticamente según el error.
    """
    t = t0
    y = y0.copy()
    dt = dt_max
    t_list = [t]
    y_list = [y.copy()]

    while t < t_end:
        if t + dt > t_end:
            dt = t_end - t

        k1 = f(t,               y)
        k2 = f(t + dt/4,        y + dt/4 * k1)
        k3 = f(t + 3*dt/8,      y + dt*(3/32*k1 + 9/32*k2))
        k4 = f(t + 12*dt/13,    y + dt*(1932/2197*k1 - 7200/2197*k2 + 7296/2197*k3))
        k5 = f(t + dt,          y + dt*(439/216*k1 - 8*k2 + 3680/513*k3 - 845/4104*k4))
        k6 = f(t + dt/2,        y + dt*(-8/27*k1 + 2*k2 - 3544/2565*k3 + 1859/4104*k4 - 11/40*k5))

        # Solución de orden 4
        y4 = y + dt * (25/216*k1 + 1408/2565*k3 + 2197/4104*k4 - 1/5*k5)
        # Solución de orden 5
        y5 = y + dt * (16/135*k1 + 6656/12825*k3 + 28561/56430*k4 - 9/50*k5 + 2/55*k6)

        # Error entre orden 4 y 5
        error = np.linalg.norm(y5 - y4)

        if error < tol:
            t = t + dt
            y = y5
            t_list.append(t)
            y_list.append(y.copy())

        # Ajustar paso de tiempo
        if error > 0:
            dt = dt * min(2.0, max(0.5, 0.9 * (tol / error) ** 0.2))
        dt = np.clip(dt, dt_min, dt_max)

    return np.array(t_list), np.array(y_list)