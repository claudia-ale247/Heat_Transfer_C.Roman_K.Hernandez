"""
Ejercicio 5-34 (v1) - Conduccion 1D estacionaria en pared compuesta (diferencias finitas).

Coordenada x: desde la superficie inferior del metal (x = 0) hasta la superficie
superior del no metal (x = 0.050 m). Nodos 0..10; el nodo 6 es la interfaz (x = 0.030 m).

Uso:  python3 ej_5_34_v1.py        (requiere numpy y matplotlib)
Salidas: texto en consola y el archivo T_vs_x_5_34_v1.png
"""
from fractions import Fraction as F

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------
# 1. Datos
# ----------------------------------------------------------------------------
k_m, L_m = 36.0, 0.030      # W/(m K), m   (metal, SB-96)
k_n, L_n = 0.05, 0.020      # W/(m K), m   (no metal)
q_in = 150.0                # W/m^2, flujo impuesto hacia el interior en x = 0
h = 5.0                     # W/(m^2 K), solo convección
T_inf = 15.0                # °C
dx = 0.005                  # m
T_lim = 93.0                # °C, límite indicado en el enunciado para el metal

N = 11                      # nodos 0..10
I_INT = 6                   # nodo de la interfaz
x = np.arange(N) * dx       # posiciones [m]
assert abs(x[I_INT] - L_m) < 1e-12 and abs(x[-1] - (L_m + L_n)) < 1e-12


def conductividad_tramo(i):
    """k del tramo entre el nodo i e i+1 (i = 0..9): metal si i < 6, no metal si i >= 6."""
    return k_m if i < I_INT else k_n


# ----------------------------------------------------------------------------
# 2. Sistema de 11 ecuaciones, todas como balances de flujo por unidad de área [W/m^2]
#    Convención: cada término es una ENTRADA positiva al nodo (k (T_vecino - T_nodo)/dx).
#    Fila i:  sum(entradas) = 0   ->   A T = b
#    Los nodos interiores se escriben multiplicando T_{i-1} - 2 T_i + T_{i+1} = 0 por k/dx.
# ----------------------------------------------------------------------------
def ensamblar(h_val):
    A = np.zeros((N, N))
    b = np.zeros(N)
    # nodo 0: q_in + k_m (T1 - T0)/dx = 0
    A[0, 0], A[0, 1], b[0] = -k_m / dx, k_m / dx, -q_in
    # nodos interiores del metal (1..5) y del no metal (7..9)
    for i in list(range(1, I_INT)) + list(range(I_INT + 1, N - 1)):
        k = k_m if i < I_INT else k_n
        A[i, i - 1], A[i, i], A[i, i + 1] = k / dx, -2 * k / dx, k / dx
    # interfaz (nodo 6): k_m (T5 - T6)/dx + k_n (T7 - T6)/dx = 0
    A[6, 5], A[6, 6], A[6, 7] = k_m / dx, -(k_m + k_n) / dx, k_n / dx
    # nodo 10: k_n (T9 - T10)/dx + h (T_inf - T10) = 0
    A[10, 9], A[10, 10], b[10] = k_n / dx, -(k_n / dx + h_val), -h_val * T_inf
    return A, b


A, b = ensamblar(h)
T = np.linalg.solve(A, b)          # temperaturas numéricas sin redondear [°C]

print("=" * 70)
print("TEMPERATURAS (solución numérica, np.linalg.solve)")
print("=" * 70)
print(f"{'Nodo':>4} {'x [mm]':>8} {'T [°C]':>14}")
for i in range(N):
    print(f"{i:4d} {x[i]*1e3:8.1f} {T[i]:14.9f}")

# ----------------------------------------------------------------------------
# 3. Flujos entre nodos y flujo convectivo
# ----------------------------------------------------------------------------
print("\n" + "=" * 70)
print("FLUJOS DE CALOR  q''_{i->i+1} = k (T_i - T_{i+1})/dx   [W/m^2]")
print("=" * 70)
flujos = np.array([conductividad_tramo(i) * (T[i] - T[i + 1]) / dx for i in range(N - 1)])
for i, qf in enumerate(flujos):
    print(f" tramo {i:2d}->{i+1:2d}: {qf:.9f}")
q_conv = h * (T[-1] - T_inf)
print(f" convección h (T10 - T_inf): {q_conv:.9f}")
print(f" flujo impuesto q_in       : {q_in:.9f}")

# ----------------------------------------------------------------------------
# 4. Residuos de los 11 balances [W/m^2] con las temperaturas numéricas sin redondear
#    Residuo = desequilibrio al sustituir T en la ecuación: r = A T - b.
# ----------------------------------------------------------------------------
r = A @ T - b
print("\n" + "=" * 70)
print("RESIDUOS DE LOS 11 BALANCES [W/m^2]  (T numéricas sin redondear)")
print("=" * 70)
for i in range(N):
    print(f" nodo {i:2d}: {r[i]: .3e}")
print(f" |r| máximo: {np.abs(r).max():.3e} W/m^2")

# ----------------------------------------------------------------------------
# 5. Solución independiente por resistencias térmicas por unidad de área R'' [m^2 K/W]
#    (R = R''/A en K/W). Con q'' = 150 W/m^2 constante en toda la cadena.
# ----------------------------------------------------------------------------
Rpp_m, Rpp_n, Rpp_c = L_m / k_m, L_n / k_n, 1.0 / h
T10_R = T_inf + q_in * Rpp_c
T6_R = T10_R + q_in * Rpp_n
T0_R = T6_R + q_in * Rpp_m
# perfil lineal dentro de cada material
T_R = np.empty(N)
for i in range(N):
    if x[i] <= L_m + 1e-12:
        T_R[i] = T0_R - q_in * x[i] / k_m
    else:
        T_R[i] = T6_R - q_in * (x[i] - L_m) / k_n

print("\n" + "=" * 70)
print("RESISTENCIAS POR UNIDAD DE ÁREA R'' [m^2 K/W] y SOLUCIÓN INDEPENDIENTE")
print("=" * 70)
print(f" R''_metal = L_m/k_m = {Rpp_m:.9e}")
print(f" R''_no metal = L_n/k_n = {Rpp_n:.9f}")
print(f" R''_conv = 1/h = {Rpp_c:.9f}")
print(f" T10 = {T10_R:.9f}  T6 = {T6_R:.9f}  T0 = {T0_R:.9f}  [°C]")
dif = np.abs(T - T_R)
print(f" max |T_numérica - T_resistencias| = {dif.max():.3e} °C")

# ----------------------------------------------------------------------------
# 6. Pendientes y caídas de temperatura
# ----------------------------------------------------------------------------
print("\n" + "=" * 70)
print("PENDIENTES (q'' = -k dT/dx) Y CAÍDAS")
print("=" * 70)
print(f" dT/dx metal    = {-q_in / k_m:.6f} K/m")
print(f" dT/dx no metal = {-q_in / k_n:.6f} K/m")
print(f" caída en el metal    T0-T6  = {T[0] - T[6]:.9f} °C")
print(f" caída en el no metal T6-T10 = {T[6] - T[10]:.9f} °C")
print(f" superficie exterior - aire T10-T_inf = {T[10] - T_inf:.9f} °C")
print(f" T0 - T_inf (total) = {T[0] - T_inf:.9f} °C")

# ----------------------------------------------------------------------------
# 7. Evaluación del límite y h umbral
# ----------------------------------------------------------------------------
def T0_de_h(h_val):
    """T máxima del metal (nodo 0) para un h dado, resolviendo el sistema completo."""
    A_, b_ = ensamblar(h_val)
    return np.linalg.solve(A_, b_)[0]


print("\n" + "=" * 70)
print("LÍMITE DE 93 °C Y h UMBRAL")
print("=" * 70)
print(f" T_max = T0 = {T[0]:.9f} °C ; exceso sobre el límite = {T[0] - T_lim:.9f} °C")
print(f" ¿T_max < {T_lim} °C?  {T[0] < T_lim}")

# valor exacto con fracciones: 1/h* = (T_lim - T_inf)/q'' - L_n/k_n - L_m/k_m
inv_h = (F(93) - F(15)) / F(150) - F(20, 1000) / F(5, 100) - F(30, 1000) / F(36)
h_star = 1 / inv_h
print(f" h* exacto = {h_star} = {float(h_star):.9f} W/(m^2 K)")
h_star_f = float(h_star)
print(f" T0(h*)            = {T0_de_h(h_star_f):.9f} °C   (alcanza el límite)")
print(f" T0(h* + 0.001)    = {T0_de_h(h_star_f + 1e-3):.9f} °C   (< 93)")
print(f" T0(8.39 redondeado a la baja) = {T0_de_h(8.39):.9f} °C   (> 93)")
print(f" T0(8.3916)        = {T0_de_h(8.3916):.9f} °C   (> 93)")
print(f" T0(h = 8.5)       = {T0_de_h(8.5):.9f} °C")
print(f"    margen respecto al límite con h = 8.5: {T_lim - T0_de_h(8.5):.9f} °C")

# ----------------------------------------------------------------------------
# 8. Gráfica
# ----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5.6))
xm = x * 1e3
ax.axvspan(0, 30, color="tab:blue", alpha=0.12)
ax.axvspan(30, 50, color="tab:orange", alpha=0.12)
ax.axvline(30, color="gray", ls=":", lw=1.2)
ax.plot(xm, T, "o-", color="black", label="Diferencias finitas (h = 5 W/(m²·K))")
ax.axhline(T_lim, color="red", ls="--", label="Límite 93 °C")
ax.text(1, 112, "Metal SB-96\nk = 36 W/(m·K)", fontsize=9, va="top")
ax.text(31, 112, "No metal\nk = 0.05 W/(m·K)", fontsize=9, va="top")
ax.text(30.5, 47, "Interfaz\n(x = 30 mm)", fontsize=8, color="dimgray")
ax.set_xlim(0, 50)
ax.set_ylim(40, 115)
ax.set_xlabel("x [mm]")
ax.set_ylabel("T [°C]")
ax.set_title("Ejercicio 5-34: T(x) en estado estacionario")
ax.grid(alpha=0.3)
ax.legend(loc="center left", bbox_to_anchor=(0.01, 0.60))

# ampliación dentro del metal
axin = ax.inset_axes([0.13, 0.08, 0.40, 0.34])
mask = xm <= 30.0001
axin.plot(xm[mask], T[mask], "o-", color="black", ms=4)
axin.set_title("Ampliación del metal (0–30 mm)", fontsize=8)
axin.set_xlabel("x [mm]", fontsize=7)
axin.set_ylabel("T [°C]", fontsize=7, labelpad=2)
axin.tick_params(labelsize=7)
axin.set_ylim(T[6] - 0.02, T[0] + 0.02)
axin.grid(alpha=0.3)

fig.tight_layout()
fig.savefig("T_vs_x_5_34_v1.png", dpi=150)
print("\nGráfica guardada: T_vs_x_5_34_v1.png")
