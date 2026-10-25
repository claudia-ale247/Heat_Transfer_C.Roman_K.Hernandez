"""
Ejercicio modificado 5-34 (v1): analisis transitorio y mejora del enfriamiento.

Autoras del proyecto: Karina Hernandez Cruz y Claudia Roman Garcia.

Modelo: conduccion 1D transitoria en pared compuesta, por unidad de area (W/m^2, J/m^2).
    x = 0 : superficie inferior de la placa SB-96;  +x hacia la superficie superior (aire).
    Caso A: SB-96 (30 mm) + capa no metalica (20 mm), h = 5 W/(m^2 K).
    Caso B: SB-96 (30 mm) + aluminio (5 mm),         h = 25 W/(m^2 K).
    Prueba I  (calentamiento): T(x,0) = 15 C, flujo q'' = 150 W/m^2 en x = 0.
    Prueba II (enfriamiento) : T(x,0) = 90 C, flujo en x = 0 igual a cero (adiabatica).

Metodos:
    - Esquema EXPLICITO de balances nodales conservativos (resultado base).
    - Solucion del MISMO sistema nodal con integracion temporal exacta (diagonalizacion),
      usada para aislar el error espacial (estudio de malla). No es una solucion exacta del
      problema continuo.
    - Aproximacion de capacidad concentrada (modelo aparte, no ajustado al nodal).

Dependencias: Python 3, numpy, scipy, matplotlib.
Ejecucion:    python3 ej_5_34_modificado_v1.py
Salidas (en el directorio de trabajo): resultados_modificado_v1.csv, convergencia_modificado_v1.csv,
    esquema_casos_modificado_v1.png, calentamiento_modificado_v1.png,
    calentamiento_normalizado_modificado_v1.png, enfriamiento_modificado_v1.png
Tiempo de ejecucion tipico: de uno a varios minutos.
"""
import csv

import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

# =============================================================================
# 1. DATOS Y SUPUESTOS (identificables)
# =============================================================================
# --- Datos del ejercicio original ---
K_M, L_M = 36.0, 0.030          # W/(m K), m      placa SB-96
K_N, L_N = 0.050, 0.020         # W/(m K), m      capa no metalica (caso A)
H_A = 5.0                       # W/(m^2 K)       convección del ejercicio original
T_INF = 15.0                    # C
Q_IN = 150.0                    # W/m^2           flujo impuesto en x = 0 (calentamiento)
T_LIM = 93.0                    # C               limite termico indicado en el ejercicio
# --- Propiedades adicionales ADOPTADAS para el transitorio (supuestos, ver reporte) ---
RHO_M, CP_M = 8530.0, 380.0     # kg/m^3, J/(kg K)   SB-96 (valores adoptados)
RHO_N, CP_N = 86.0, 2030.0      # kg/m^3, J/(kg K)   capa no metalica (corcho como representacion)
# --- Parametros modificados por diseno (caso B) ---
K_AL, L_AL = 237.0, 0.005       # W/(m K), m      aluminio puro
RHO_AL, CP_AL = 2702.0, 903.0   # kg/m^3, J/(kg K)
H_B = 25.0                      # W/(m^2 K)       condicion de diseno
# --- Condiciones elegidas para la comparacion (no son datos del ejercicio original) ---
T_I_CAL = 15.0                  # C, inicial de la prueba de calentamiento
T_I_ENF = 90.0                  # C, inicial de la prueba de enfriamiento
T_OBJ_ENF = 60.0                # C, objetivo de la prueba de enfriamiento
FRAC = 0.95                     # fraccion para t95
# --- Mallas y pasos base ---
DX_BASE = 0.005                 # m
DT_BASE = {"A": 1.0, "B": 0.1}  # s
DT_ESTUDIO = {"A": [1.0, 0.5, 0.25], "B": [0.1, 0.05, 0.025]}
DX_ESTUDIO = [0.005, 0.0025, 0.00125, 0.000625]

CASOS = {
    "A": dict(sup=dict(k=K_N, rho=RHO_N, cp=CP_N, L=L_N), h=H_A,
              nombre="Caso A (original)"),
    "B": dict(sup=dict(k=K_AL, rho=RHO_AL, cp=CP_AL, L=L_AL), h=H_B,
              nombre="Caso B (modificado)"),
}
MET = dict(k=K_M, rho=RHO_M, cp=CP_M, L=L_M)


# =============================================================================
# 2. MALLA Y SISTEMA NODAL:  C dT/dt = -K T + f      (por unidad de area)
# =============================================================================
def malla(caso, dx):
    """Nodos 0..N-1. Intervalo j (entre nodo j y j+1) pertenece al metal si j < n_m.
    C_i suma, para cada intervalo adyacente, (rho cp)*dx/2: asi las superficies usan medio
    volumen y la interfaz suma la contribucion de ambos materiales."""
    c = CASOS[caso]
    sup = c["sup"]
    n_m = int(round(MET["L"] / dx))
    n_s = int(round(sup["L"] / dx))
    assert abs(n_m * dx - MET["L"]) < 1e-9 and abs(n_s * dx - sup["L"]) < 1e-9
    N = n_m + n_s + 1
    k_int = np.array([MET["k"]] * n_m + [sup["k"]] * n_s)
    rc_int = np.array([MET["rho"] * MET["cp"]] * n_m + [sup["rho"] * sup["cp"]] * n_s)
    G = k_int / dx                                  # conductancia de cada intervalo [W/(m^2 K)]
    C = np.zeros(N)
    for j in range(N - 1):
        C[j] += rc_int[j] * dx / 2
        C[j + 1] += rc_int[j] * dx / 2              # [J/(m^2 K)]
    K = np.zeros((N, N))
    for j in range(N - 1):
        K[j, j] += G[j]; K[j + 1, j + 1] += G[j]
        K[j, j + 1] -= G[j]; K[j + 1, j] -= G[j]
    K[N - 1, N - 1] += c["h"]
    x = np.arange(N) * dx
    return dict(caso=caso, dx=dx, N=N, i_int=n_m, x=x, G=G, C=C, K=K, h=c["h"],
                k_int=k_int, rc_int=rc_int)


def vector_f(m, calentando):
    f = np.zeros(m["N"])
    f[0] = Q_IN if calentando else 0.0              # flujo impuesto en x = 0
    f[-1] = m["h"] * T_INF                          # termino convectivo h T_inf
    return f


def dt_limite_por_nodo(m):
    """Criterio de coeficientes no negativos de T_i^p: 1 - dt K_ii / C_i >= 0."""
    return m["C"] / np.diag(m["K"])


# =============================================================================
# 3. ESQUEMA EXPLICITO
# =============================================================================
def corrida_explicita(m, T0, f, dt, objetivos=(), t_fin=None, t_max=None, snaps=()):
    """Avanza T^{p+1} = T^p + dt/C (f - K T^p). Detecta cruces de la temperatura maxima del
    sistema (interpolacion lineal entre pasos). Acumula el balance global de energia.
    objetivos: lista de (nombre, valor, sentido) con sentido +1 (sube) o -1 (baja)."""
    N = m["N"]; C = m["C"]
    Mexp = np.eye(N) - dt * (m["K"] / C[:, None])
    g = dt * f / C
    T = T0.copy()
    E0 = float(C @ T)
    pend = list(objetivos); cruces = {}
    paso_snaps = {int(round(t / dt)): t for t in snaps}
    snapshots = {}
    hist_t, hist = [0.0], [T.copy()]
    cada = max(1, int(round(60.0 / dt))) if dt >= 0.5 else max(1, int(round(6.0 / dt)))
    suma_top = 0.0
    p = 0
    mp = T.max()
    limite = int(round((t_fin if t_fin is not None else t_max) / dt))
    while p < limite:
        suma_top += T[-1] - T_INF                    # flujo saliente con T^p
        T = Mexp @ T
        T += g
        p += 1
        mx = T.max()
        for ob in list(pend):
            nom, val, s = ob
            if (mx - val) * s >= 0:
                cruces[nom] = (p - 1) * dt + dt * (val - mp) / (mx - mp)
                pend.remove(ob)
        mp = mx
        if p in paso_snaps:
            snapshots[paso_snaps[p]] = T.copy()
        if p % cada == 0:
            hist_t.append(p * dt); hist.append(T.copy())
        if t_fin is None and not pend:
            break
    t_fin_real = p * dt
    Q_out = m["h"] * suma_top * dt
    Q_in = f[0] * t_fin_real
    dE = float(C @ T) - E0
    return dict(cruces=cruces, T=T, t=t_fin_real, hist_t=np.array(hist_t), hist=np.array(hist),
                Q_in=Q_in, Q_out=Q_out, dE=dE, res_bal=dE - (Q_in - Q_out), snapshots=snapshots,
                completo=(len(pend) == 0))


# =============================================================================
# 4. MISMO SISTEMA NODAL CON INTEGRACION TEMPORAL EXACTA (diagonalizacion)
#    y = C^{1/2}(T - T_ss),  dy/dt = -S y,  S = C^{-1/2} K C^{-1/2} (simetrica)
# =============================================================================
def solucion_exacta_en_tiempo(m, T0, f):
    C = m["C"]
    Tss = np.linalg.solve(m["K"], f)
    s = 1.0 / np.sqrt(C)
    S = s[:, None] * m["K"] * s[None, :]
    lam, V = np.linalg.eigh(S)
    y0 = V.T @ (np.sqrt(C) * (T0 - Tss))

    def T_de_t(t):
        return Tss + s * (V @ (np.exp(-lam * t) * y0))
    return Tss, lam, T_de_t


def tiempo_cruce(Tmax_de_t, valor, sentido, lam_min):
    """Raiz de Tmax(t) = valor (funcion monotona en estas pruebas)."""
    g = lambda t: Tmax_de_t(t) - valor
    t_hi = 1.0 / lam_min
    for _ in range(40):
        if g(t_hi) * sentido >= 0:
            break
        t_hi *= 2
    else:
        return np.nan
    return brentq(g, 0.0, t_hi, xtol=1e-9, rtol=1e-13)


def metricas_exactas(caso, dx):
    m = malla(caso, dx)
    N = m["N"]
    # calentamiento
    f_c = vector_f(m, True)
    T0c = np.full(N, T_I_CAL)
    Tss, lam, Tc = solucion_exacta_en_tiempo(m, T0c, f_c)
    Tmax_c = lambda t: Tc(t).max()
    Tmax_ss = Tss.max()
    out = dict(dx=dx, N=N, Tmax_ss=Tmax_ss, nodo_max_ss=int(np.argmax(Tss)),
               tau_lento=1.0 / lam.min())
    out["t95"] = tiempo_cruce(Tmax_c, T_I_CAL + FRAC * (Tmax_ss - T_I_CAL), +1, lam.min())
    out["t93"] = tiempo_cruce(Tmax_c, T_LIM, +1, lam.min()) if Tmax_ss > T_LIM else np.nan
    # enfriamiento
    f_e = vector_f(m, False); f_e[0] = 0.0
    T0e = np.full(N, T_I_ENF)
    Tss_e, lam_e, Te = solucion_exacta_en_tiempo(m, T0e, f_e)
    Tmax_e = lambda t: Te(t).max()
    out["t_enf"] = tiempo_cruce(Tmax_e, T_OBJ_ENF, -1, lam_e.min())
    return out, dict(m=m, Tc=Tc, Te=Te, Tss=Tss)


# =============================================================================
# 5. APROXIMACION DE CAPACIDAD CONCENTRADA (derivada en el reporte)
#    C'' dT/dt = q_in - (T - T_inf)/R''_ext ;   T(t) = T_ss + (T_i - T_ss) exp(-t/tau)
# =============================================================================
def concentrado(caso, incluir_capa_sup=True):
    c = CASOS[caso]; s = c["sup"]
    if caso == "A" and not incluir_capa_sup:
        C_ = MET["rho"] * MET["cp"] * MET["L"]
        R_ext = s["L"] / s["k"] + 1.0 / c["h"]
    elif caso == "A":
        C_ = MET["rho"] * MET["cp"] * MET["L"] + s["rho"] * s["cp"] * s["L"]
        R_ext = s["L"] / s["k"] + 1.0 / c["h"]
    else:                                            # B: ambas capas, resistencia externa 1/h
        C_ = MET["rho"] * MET["cp"] * MET["L"] + s["rho"] * s["cp"] * s["L"]
        R_ext = 1.0 / c["h"]
    tau = C_ * R_ext
    Tss_c = T_INF + Q_IN * R_ext
    return dict(C=C_, R_ext=R_ext, tau=tau, Tss=Tss_c,
                t95=-tau * np.log(1 - FRAC),
                t93=(-tau * np.log(1 - (T_LIM - T_I_CAL) / (Tss_c - T_I_CAL))
                     if Tss_c > T_LIM else np.nan),
                t_enf=tau * np.log((T_I_ENF - T_INF) / (T_OBJ_ENF - T_INF)),
                T_de_t_cal=lambda t: Tss_c + (T_I_CAL - Tss_c) * np.exp(-t / tau),
                T_de_t_enf=lambda t: T_INF + (T_I_ENF - T_INF) * np.exp(-t / tau))


# =============================================================================
# 6. PROGRAMA PRINCIPAL
# =============================================================================
def main():
    R = {}                                           # resultados para el reporte
    filas = []                                       # resultados_modificado_v1.csv
    conv_filas = []                                  # convergencia_modificado_v1.csv

    def reg(caso, prueba, magnitud, metodo, valor, unidad, malla_, dt_, nota=""):
        filas.append([caso, prueba, magnitud, metodo, valor, unidad, malla_, dt_, nota])

    print("=" * 78)
    print("1. PROPIEDADES DERIVADAS (por unidad de area)")
    print("=" * 78)
    prop = {}
    for caso, c in CASOS.items():
        s = c["sup"]
        d = dict(
            alpha_m=MET["k"] / (MET["rho"] * MET["cp"]),
            alpha_s=s["k"] / (s["rho"] * s["cp"]),
            Rpp_m=MET["L"] / MET["k"], Rpp_s=s["L"] / s["k"], Rpp_conv=1.0 / c["h"],
            C_m=MET["rho"] * MET["cp"] * MET["L"], C_s=s["rho"] * s["cp"] * s["L"],
            rc_m=MET["rho"] * MET["cp"], rc_s=s["rho"] * s["cp"])
        d["Rpp_tot"] = d["Rpp_m"] + d["Rpp_s"] + d["Rpp_conv"]
        d["C_tot"] = d["C_m"] + d["C_s"]
        d["Tmax_ss_res"] = T_INF + Q_IN * d["Rpp_tot"]
        d["T_bi_in_ss"] = None
        prop[caso] = d
        print(f"Caso {caso}: alpha_m={d['alpha_m']:.4e} alpha_sup={d['alpha_s']:.4e} m^2/s")
        print(f"   R''_m={d['Rpp_m']:.6e} R''_sup={d['Rpp_s']:.6e} R''_conv={d['Rpp_conv']:.6f} "
              f"R''_tot={d['Rpp_tot']:.6e} m^2K/W")
        print(f"   C''_m={d['C_m']:.2f} C''_sup={d['C_s']:.2f} C''_tot={d['C_tot']:.2f} J/(m^2K)")
        print(f"   T_max,ss (resistencias) = {d['Tmax_ss_res']:.6f} C")
        reg(caso, "-", "alpha metal", "formula", d["alpha_m"], "m2/s", "", "")
        reg(caso, "-", "alpha capa superior", "formula", d["alpha_s"], "m2/s", "", "")
        reg(caso, "-", "R'' metal", "formula", d["Rpp_m"], "m2K/W", "", "")
        reg(caso, "-", "R'' capa superior", "formula", d["Rpp_s"], "m2K/W", "", "")
        reg(caso, "-", "R'' conveccion", "formula", d["Rpp_conv"], "m2K/W", "", "")
        reg(caso, "-", "R'' total", "formula", d["Rpp_tot"], "m2K/W", "", "")
        reg(caso, "-", "C'' metal", "formula", d["C_m"], "J/(m2K)", "", "")
        reg(caso, "-", "C'' capa superior", "formula", d["C_s"], "J/(m2K)", "", "")
        reg(caso, "-", "C'' total", "formula", d["C_tot"], "J/(m2K)", "", "")
        reg(caso, "I", "Tmax estacionaria", "resistencias", d["Tmax_ss_res"], "C", "", "")
    R["prop"] = prop

    # ---- Biot y Fourier ----
    bi = {}
    bi["A_capa_sup_conv"] = H_A * L_N / K_N
    bi["A_metal_eff"] = prop["A"]["Rpp_m"] / (prop["A"]["Rpp_s"] + prop["A"]["Rpp_conv"])
    bi["B_conj_eff"] = (prop["B"]["Rpp_m"] + prop["B"]["Rpp_s"]) / prop["B"]["Rpp_conv"]
    bi["B_al_conv"] = H_B * L_AL / K_AL
    bi["B_metal_conv_h"] = H_B * L_M / K_M
    R["bi"] = bi
    print("\nBiot: ", {k: f"{v:.4e}" for k, v in bi.items()})
    for k, v in bi.items():
        reg("A" if k.startswith("A") else "B", "-", "Biot " + k, "formula", v, "-", "", "")

    # ---- Estabilidad por tipo de nodo, mallas base ----
    print("\n" + "=" * 78)
    print("2. LIMITE DE ESTABILIDAD DEL ESQUEMA EXPLICITO (malla base 5 mm)")
    print("=" * 78)
    estab = {}
    for caso in CASOS:
        m = malla(caso, DX_BASE)
        lim = dt_limite_por_nodo(m)
        i_lim = int(np.argmin(lim))
        estab[caso] = dict(lim=lim, i_lim=i_lim, dt_max=float(lim.min()), N=m["N"], i_int=m["i_int"])
        print(f"Caso {caso}: N={m['N']} nodos, interfaz nodo {m['i_int']}; dt limite por nodo [s]:")
        print("   " + " ".join(f"{i}:{v:.4f}" for i, v in enumerate(lim)))
        print(f"   limitante: nodo {i_lim}, dt_max = {lim.min():.5f} s ; dt base = {DT_BASE[caso]} s")
        reg(caso, "-", "dt maximo explicito (malla base)", "criterio nodal", float(lim.min()), "s",
            "5 mm", DT_BASE[caso], f"nodo limitante {i_lim}")
    R["estab"] = estab

    # ---- Ejemplo a mano: primeros dos pasos de A (calentamiento) ----
    mA = malla("A", DX_BASE); fA = vector_f(mA, True)
    T0 = np.full(mA["N"], T_I_CAL)
    r2 = corrida_explicita(mA, T0, fA, 1.0, t_fin=2.0, snaps=(1.0, 2.0))
    R["paso12"] = {t: s.copy() for t, s in r2["snapshots"].items()}
    R["CA"] = mA["C"].copy()
    print("\n" + "=" * 78)
    print("3. PRIMEROS DOS PASOS, CASO A, CALENTAMIENTO (dt = 1 s)")
    print("=" * 78)
    print("C_i [J/(m^2K)]:", np.array2string(mA["C"], precision=4))
    for t in (1.0, 2.0):
        print(f"t = {t:.0f} s:", np.array2string(r2["snapshots"][t], precision=9))
    # Enfriamiento: primer paso de A con flujo 0 desde 90 C (efecto del cambio en el balance inferior)
    fAe = vector_f(mA, False)
    r1e = corrida_explicita(mA, np.full(mA["N"], T_I_ENF), fAe, 1.0, t_fin=1.0, snaps=(1.0,))
    print("Enfriamiento A, t = 1 s:", np.array2string(r1e["snapshots"][1.0], precision=9))
    R["paso1_enf"] = r1e["snapshots"][1.0].copy()

    # ---- Resultados base: explicito, malla 5 mm ----
    print("\n" + "=" * 78)
    print("4. RESULTADOS BASE (esquema explicito, malla 5 mm)")
    print("=" * 78)
    base = {}
    snaps_cal = {"A": [h * 3600.0 for h in (0.5, 1, 2, 4, 8, 16, 24, 33, 48)],
                 "B": [mn * 60.0 for mn in (0.5, 1, 2, 5, 10, 20, 40, 60)]}
    snaps_enf = {"A": [h * 3600.0 for h in (0.5, 1, 2, 4, 6, 8)],
                 "B": [mn * 60.0 for mn in (1, 2, 5, 10, 20, 30)]}
    for caso in CASOS:
        m = malla(caso, DX_BASE); dt = DT_BASE[caso]; N = m["N"]
        Tss = np.linalg.solve(m["K"], vector_f(m, True))
        Tmax_ss = Tss.max()
        obj = [("t95", T_I_CAL + FRAC * (Tmax_ss - T_I_CAL), +1)]
        if Tmax_ss > T_LIM:
            obj.append(("t93", T_LIM, +1))
        rc = corrida_explicita(m, np.full(N, T_I_CAL), vector_f(m, True), dt, objetivos=obj,
                               t_max=400 * 3600.0, snaps=snaps_cal[caso])
        # t95 puede ser posterior al cruce de 93: se continua hasta tener ambos
        fe = vector_f(m, False)
        re_ = corrida_explicita(m, np.full(N, T_I_ENF), fe, dt,
                                objetivos=[("t_enf", T_OBJ_ENF, -1)], t_max=100 * 3600.0,
                                snaps=snaps_enf[caso])
        base[caso] = dict(m=m, dt=dt, Tss=Tss, Tmax_ss=Tmax_ss, cal=rc, enf=re_)
        print(f"Caso {caso}: Tmax,ss nodal = {Tmax_ss:.6f} C (nodo {int(np.argmax(Tss))}); "
              f"T interfaz ss = {Tss[m['i_int']]:.6f}; T superficie sup ss = {Tss[-1]:.6f}")
        print(f"   calentamiento: cruces = { {k: f'{v:.3f} s = {v/3600:.5f} h' for k, v in rc['cruces'].items()} }")
        print(f"   enfriamiento : t_60 = {re_['cruces'].get('t_enf', float('nan')):.3f} s = "
              f"{re_['cruces'].get('t_enf', float('nan'))/3600:.5f} h")
        print(f"   balance calentamiento: Qin={rc['Q_in']:.4f} Qout={rc['Q_out']:.4f} "
              f"dE={rc['dE']:.4f} res={rc['res_bal']:.3e} J/m2")
        print(f"   balance enfriamiento : Qout={re_['Q_out']:.4f} dE={re_['dE']:.4f} "
              f"res={re_['res_bal']:.3e} J/m2")
        reg(caso, "I", "Tmax estacionaria nodal", "nodal (sistema estacionario)", Tmax_ss, "C",
            "5 mm", "", "nodo 0")
        for k, v in rc["cruces"].items():
            reg(caso, "I", {"t93": "tiempo para 93 C", "t95": "t95 (Tmax)"}[k],
                "explicito", v, "s", "5 mm", dt)
            reg(caso, "I", {"t93": "tiempo para 93 C", "t95": "t95 (Tmax)"}[k] + " [h]",
                "explicito", v / 3600.0, "h", "5 mm", dt)
        reg(caso, "II", "tiempo de enfriamiento 90->60 C", "explicito",
            re_["cruces"]["t_enf"], "s", "5 mm", dt)
        reg(caso, "II", "tiempo de enfriamiento 90->60 C [h]", "explicito",
            re_["cruces"]["t_enf"] / 3600.0, "h", "5 mm", dt)
        reg(caso, "I", "residuo balance global", "explicito", rc["res_bal"], "J/m2", "5 mm", dt)
        reg(caso, "II", "residuo balance global", "explicito", re_["res_bal"], "J/m2", "5 mm", dt)
    R["base"] = base
    tA, tB = base["A"]["enf"]["cruces"]["t_enf"], base["B"]["enf"]["cruces"]["t_enf"]
    R["cmp_enf_base"] = dict(tA=tA, tB=tB, dif=tA - tB, factor=tA / tB, red=100 * (tA - tB) / tA)
    print(f"\nENFRIAMIENTO (malla base explicita): tA={tA:.2f} s, tB={tB:.2f} s, "
          f"dif={tA-tB:.2f} s, factor={tA/tB:.4f}, reduccion={100*(tA-tB)/tA:.4f} %")
    for k, v in R["cmp_enf_base"].items():
        reg("A/B", "II", "comparacion enfriamiento: " + k, "explicito", v,
            {"tA": "s", "tB": "s", "dif": "s", "factor": "-", "red": "%"}[k], "5 mm", "")

    # ---- Calentamiento: donde esta el maximo y recuperacion estacionaria ----
    print("\n" + "=" * 78)
    print("5. COMPROBACIONES")
    print("=" * 78)
    chk = {}
    for caso in CASOS:
        b = base[caso]; m = b["m"]; N = m["N"]; dt = b["dt"]
        # (a) ubicacion del maximo en las corridas
        idx_cal = np.argmax(b["cal"]["hist"], axis=1)
        idx_enf = np.argmax(b["enf"]["hist"], axis=1)
        # (b) recuperacion del estacionario con la corrida explicita larga
        t_largo = 700000.0 if caso == "A" else 60000.0
        rl = corrida_explicita(m, np.full(N, T_I_CAL), vector_f(m, True), dt, t_fin=t_largo)
        dif_ss = np.abs(rl["T"] - b["Tss"]).max()
        # (c) estado estacionario como condicion inicial permanece
        rs = corrida_explicita(m, b["Tss"].copy(), vector_f(m, True), dt, t_fin=2000 * dt)
        mant = np.abs(rs["T"] - b["Tss"]).max()
        # (d) prueba nula: T = T_inf sin calentamiento no cambia
        fnul = vector_f(m, False)
        rn = corrida_explicita(m, np.full(N, T_INF), fnul, dt, t_fin=2000 * dt)
        nulo = np.abs(rn["T"] - T_INF).max()
        # (e) flujos en el estacionario: continuidad en la interfaz y salida convectiva
        Tss = b["Tss"]
        q_izq = m["G"][m["i_int"] - 1] * (Tss[m["i_int"] - 1] - Tss[m["i_int"]])
        q_der = m["G"][m["i_int"]] * (Tss[m["i_int"]] - Tss[m["i_int"] + 1])
        q_conv = m["h"] * (Tss[-1] - T_INF)
        # (f) solucion estacionaria por resistencias
        d = prop[caso]
        T_top_R = T_INF + Q_IN * d["Rpp_conv"]
        T_int_R = T_top_R + Q_IN * d["Rpp_s"]
        T_0_R = T_int_R + Q_IN * d["Rpp_m"]
        dif_R = max(abs(Tss[0] - T_0_R), abs(Tss[m["i_int"]] - T_int_R), abs(Tss[-1] - T_top_R))
        chk[caso] = dict(nodo_max_cal=sorted(set(idx_cal.tolist())), nodo_max_enf=sorted(set(idx_enf.tolist())),
                         t_largo=t_largo, dif_ss=dif_ss, mant=mant, nulo=nulo,
                         q_izq=q_izq, q_der=q_der, q_conv=q_conv, T0R=T_0_R, TintR=T_int_R,
                         TtopR=T_top_R, dif_R=dif_R)
        print(f"Caso {caso}: nodo del maximo (calent.)={chk[caso]['nodo_max_cal']}, (enfr.)={chk[caso]['nodo_max_enf']}")
        print(f"   |T_explicito(t={t_largo:.0f} s) - T_ss| max = {dif_ss:.3e} C")
        print(f"   permanencia del estacionario (2000 pasos): {mant:.3e} C ; prueba nula: {nulo:.3e} C")
        print(f"   flujos estacionarios: izq. interfaz={q_izq:.9f}, der.={q_der:.9f}, conv={q_conv:.9f} W/m2")
        print(f"   resistencias: T0={T_0_R:.6f} Tint={T_int_R:.6f} Ttop={T_top_R:.6f} ; dif max nodal-R = {dif_R:.3e}")
        reg(caso, "I", "recuperacion de T_ss (max |dT|)", "explicito largo", dif_ss, "C", "5 mm", dt,
            f"t = {t_largo:.0f} s")
        reg(caso, "I", "dif max nodal-resistencias (T_ss)", "comparacion", dif_R, "C", "5 mm", "")
    R["chk"] = chk

    # ---- Demostracion de inestabilidad por encima del limite ----
    print("\nDEMOSTRACION: dt por encima del limite")
    inest = {}
    for caso, dt_bad in (("A", 1.25), ("B", 0.2)):
        m = malla(caso, DX_BASE)
        r = corrida_explicita(m, np.full(m["N"], T_I_ENF), vector_f(m, False), dt_bad, t_fin=200 * dt_bad)
        inest[caso] = dict(dt=dt_bad, maxabs=float(np.abs(r["T"]).max()))
        print(f"   Caso {caso}: dt = {dt_bad} s -> max |T| tras 200 pasos = {inest[caso]['maxabs']:.3e}")
        reg(caso, "II", "max|T| tras 200 pasos con dt > limite", "explicito", inest[caso]["maxabs"], "C",
            "5 mm", dt_bad, "inestable")
    R["inest"] = inest

    # ---- Estudio de malla (integracion temporal exacta del sistema nodal) ----
    print("\n" + "=" * 78)
    print("6. ESTUDIO DE MALLA (sistema nodal con integracion temporal exacta)")
    print("=" * 78)
    malla_res = {c: [] for c in CASOS}
    for caso in CASOS:
        for dx in DX_ESTUDIO:
            mt, _ = metricas_exactas(caso, dx)
            malla_res[caso].append(mt)
            print(f"Caso {caso} dx={dx*1e3:.3f} mm N={mt['N']}: Tmax_ss={mt['Tmax_ss']:.6f} "
                  f"t93={mt['t93']/3600 if not np.isnan(mt['t93']) else float('nan'):.5f} h "
                  f"t95={mt['t95']/3600:.5f} h t_enf={mt['t_enf']/3600:.5f} h")
            for nom, key, un in (("Tmax estacionaria", "Tmax_ss", "C"), ("tiempo para 93 C", "t93", "s"),
                                 ("t95 (Tmax)", "t95", "s"), ("tiempo de enfriamiento", "t_enf", "s")):
                conv_filas.append(["malla", caso, nom, f"{dx*1e3:g}", mt["N"], "exacta en tiempo (sistema nodal)",
                                   mt[key], un, ""])
    R["malla"] = malla_res
    # paso admisible al refinar
    adm = {}
    for caso in CASOS:
        adm[caso] = []
        for dx in DX_ESTUDIO:
            m = malla(caso, dx)
            lim = dt_limite_por_nodo(m)
            adm[caso].append((dx, float(lim.min()), int(np.argmin(lim))))
            conv_filas.append(["paso admisible explicito", caso, "dt maximo", f"{dx*1e3:g}", m["N"],
                               "criterio nodal", float(lim.min()), "s", f"nodo {int(np.argmin(lim))}"])
    R["adm"] = adm

    # ---- Estudio temporal en malla base (explicito vs exacto en la misma malla) ----
    print("\n" + "=" * 78)
    print("7. SENSIBILIDAD AL PASO TEMPORAL (malla 5 mm)")
    print("=" * 78)
    temporal = {c: [] for c in CASOS}
    ref = {}
    for caso in CASOS:
        mt, _ = metricas_exactas(caso, DX_BASE)
        ref[caso] = mt
        m = malla(caso, DX_BASE); N = m["N"]
        Tmax_ss = mt["Tmax_ss"]
        for dt in DT_ESTUDIO[caso]:
            obj = [("t95", T_I_CAL + FRAC * (Tmax_ss - T_I_CAL), +1)]
            if Tmax_ss > T_LIM:
                obj.append(("t93", T_LIM, +1))
            rc = corrida_explicita(m, np.full(N, T_I_CAL), vector_f(m, True), dt, objetivos=obj,
                                   t_max=400 * 3600.0)
            re_ = corrida_explicita(m, np.full(N, T_I_ENF), vector_f(m, False), dt,
                                    objetivos=[("t_enf", T_OBJ_ENF, -1)], t_max=100 * 3600.0)
            fila = dict(dt=dt, t93=rc["cruces"].get("t93", np.nan), t95=rc["cruces"]["t95"],
                        t_enf=re_["cruces"]["t_enf"], res_cal=rc["res_bal"], res_enf=re_["res_bal"])
            temporal[caso].append(fila)
            print(f"Caso {caso} dt={dt}: t93={fila['t93']:.3f} s t95={fila['t95']:.3f} s "
                  f"t_enf={fila['t_enf']:.3f} s")
            for nom, key in (("tiempo para 93 C", "t93"), ("t95 (Tmax)", "t95"), ("tiempo de enfriamiento", "t_enf")):
                conv_filas.append(["paso temporal", caso, nom, "5", N, f"explicito dt={dt} s",
                                   fila[key], "s", ""])
        for nom, key in (("tiempo para 93 C", "t93"), ("t95 (Tmax)", "t95"), ("tiempo de enfriamiento", "t_enf")):
            conv_filas.append(["paso temporal", caso, nom, "5", N, "referencia: exacta en tiempo, misma malla",
                               mt[key], "s", ""])
    R["temporal"] = temporal; R["ref_base"] = ref

    # ---- Concentrado ----
    print("\n" + "=" * 78)
    print("8. CAPACIDAD CONCENTRADA")
    print("=" * 78)
    conc = {"A_sin": concentrado("A", False), "A_con": concentrado("A", True), "B": concentrado("B")}
    for k, c in conc.items():
        print(f"{k}: C''={c['C']:.2f} R_ext={c['R_ext']:.6f} tau={c['tau']:.2f} s = {c['tau']/3600:.4f} h; "
              f"Tss={c['Tss']:.4f}; t93={c['t93']:.1f} s; t95={c['t95']:.1f} s; t_enf={c['t_enf']:.1f} s")
        caso = k[0]
        reg(caso, "I/II", f"tau concentrado ({k})", "concentrado", c["tau"], "s", "", "")
        reg(caso, "I", f"Tss concentrado ({k})", "concentrado", c["Tss"], "C", "", "")
        reg(caso, "I", f"t95 concentrado ({k})", "concentrado", c["t95"], "s", "", "")
        if not np.isnan(c["t93"]):
            reg(caso, "I", f"tiempo para 93 C concentrado ({k})", "concentrado", c["t93"], "s", "", "")
        reg(caso, "II", f"tiempo de enfriamiento concentrado ({k})", "concentrado", c["t_enf"], "s", "", "")
    R["conc"] = conc

    # ---- Umbral h del ejercicio original (contexto) ----
    h_star = 1.0 / ((T_LIM - T_INF) / Q_IN - L_N / K_N - L_M / K_M)
    R["h_star"] = h_star
    print(f"\nh* = {h_star:.9f} W/(m2K) (1200/143 = {1200/143:.9f})")

    # ---- Energia / rapidez: consecuencia fisica ----
    R["E_ini_enf"] = {c: prop[c]["C_tot"] * (T_I_ENF - T_INF) for c in CASOS}

    # =========================================================================
    # CSV
    # =========================================================================
    with open("resultados_modificado_v1.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["caso", "prueba", "magnitud", "metodo", "valor", "unidad", "malla_mm", "dt_s", "nota"])
        for fila in filas:
            w.writerow(fila)
    with open("convergencia_modificado_v1.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["estudio", "caso", "magnitud", "dx_mm", "nodos", "metodo", "valor", "unidad", "nota"])
        for fila in conv_filas:
            w.writerow(fila)

    # =========================================================================
    # FIGURAS
    # =========================================================================
    figuras(R)
    return R


def figuras(R):
    base = R["base"]; conc = R["conc"]
    colA, colB = "tab:red", "tab:blue"
    # --- 1. Esquema ---
    fig, axs = plt.subplots(1, 2, figsize=(11, 6.2))
    for ax, caso, nombre in zip(axs, ("A", "B"), ("Caso A: sistema original", "Caso B: sistema modificado")):
        c = CASOS[caso]; Ls = c["sup"]["L"] * 1e3
        ax.add_patch(Rectangle((0, 0), 3, 30, fc="#9ecae1", ec="k"))
        ax.text(1.5, 15, "Metal SB-96\nL = 30 mm\nk = 36 W/(m·K)\nρ = 8530 kg/m³\ncp = 380 J/(kg·K)",
                ha="center", va="center", fontsize=8)
        ax.add_patch(Rectangle((0, 30), 3, Ls, fc="#fdd0a2" if caso == "A" else "#d9d9d9", ec="k"))
        if caso == "A":
            txt = "Capa no metálica\nL = 20 mm\nk = 0.05 W/(m·K)\nρ = 86 kg/m³\ncp = 2030 J/(kg·K)"
        else:
            txt = "Aluminio\nL = 5 mm\nk = 237 W/(m·K)\nρ = 2702 kg/m³\ncp = 903 J/(kg·K)"
        if caso == "A":
            ax.text(1.5, 30 + Ls / 2, txt, ha="center", va="center", fontsize=8)
        else:
            ax.text(3.4, 30 + Ls / 2 + 9, txt, ha="left", va="center", fontsize=8)
            ax.plot([3.0, 3.35], [30 + Ls / 2, 30 + Ls / 2 + 9], color="k", lw=0.7)
        ax.plot([0, 3], [30, 30], color="k", ls=":", lw=1.0)
        ax.text(3.1, 27, "interfaz (nodo 6, x = 30 mm)", fontsize=8, va="top")
        top = 30 + Ls
        ax.add_patch(FancyArrowPatch((1.5, -9), (1.5, -1), arrowstyle="-|>", mutation_scale=14, color="firebrick"))
        ax.text(1.6, -6, "Prueba I: q'' = 150 W/m² entra en x = 0\nPrueba II: q'' = 0 (adiabática)", fontsize=8, va="center")
        for xx in (0.5, 1.5, 2.5):
            ax.add_patch(FancyArrowPatch((xx, top + 1), (xx, top + 8), arrowstyle="<|-|>", mutation_scale=10, color="teal"))
        ax.text(3.4, top + (5 if caso == "A" else 21), f"convección h = {c['h']:g} W/(m²·K)\nT∞ = 15 °C", fontsize=8, va="center", color="teal")
        ax.annotate("", xy=(-0.4, top), xytext=(-0.4, 0), arrowprops=dict(arrowstyle="->"))
        ax.text(-0.5, top / 2, "x", rotation=90, ha="right", va="center", fontsize=10)
        ax.text(-0.5, 0, "x = 0", ha="right", va="bottom", fontsize=8)
        ax.text(-0.5, top, f"x = {top:g} mm", ha="right", va="top", fontsize=8)
        ax.set_xlim(-1.6, 8.5); ax.set_ylim(-12, 60); ax.axis("off")
        ax.set_title(nombre + f"  (espesor total {top:g} mm)", fontsize=10)
    fig.suptitle("Configuraciones A y B (por unidad de área, conducción 1D)", fontsize=11)
    fig.tight_layout(); fig.savefig("esquema_casos_modificado_v1.png", dpi=150); plt.close(fig)

    # --- 2. Calentamiento ---
    fig, axs = plt.subplots(1, 2, figsize=(12, 4.8))
    hA = base["A"]["cal"]; hB = base["B"]["cal"]
    ax = axs[0]
    ax.plot(hA["hist_t"] / 3600, hA["hist"].max(axis=1), color=colA, label="A, nodal explícito (T máx)")
    tt = np.linspace(0, hA["hist_t"][-1], 400)
    ax.plot(tt / 3600, conc["A_sin"]["T_de_t_cal"](tt), "--", color="gray", label="A, concentrado (metal; capa sup. sin almacenamiento)")
    ax.axhline(T_LIM, color="k", ls="--", lw=1, label="Límite 93 °C")
    ax.axhline(base["A"]["Tmax_ss"], color=colA, ls=":", lw=1)
    ax.axvline(hA["cruces"]["t93"] / 3600, color="k", ls=":", lw=0.8)
    ax.text(hA["cruces"]["t93"] / 3600 + 0.5, 30, f"93 °C a t = {hA['cruces']['t93']/3600:.1f} h", fontsize=8)
    ax.set_xlabel("t [h]"); ax.set_ylabel("Temperatura máxima [°C]"); ax.set_title("Caso A: calentamiento")
    ax.grid(alpha=0.3); ax.legend(fontsize=7, loc="lower right")
    ax = axs[1]
    ax.plot(hB["hist_t"] / 60, hB["hist"].max(axis=1), color=colB, label="B, nodal explícito (T máx)")
    tt = np.linspace(0, hB["hist_t"][-1], 400)
    ax.plot(tt / 60, conc["B"]["T_de_t_cal"](tt), "--", color="gray", label="B, concentrado (ambas capas)")
    ax.axhline(base["B"]["Tmax_ss"], color=colB, ls=":", lw=1, label=f"T máx,ss nodal = {base['B']['Tmax_ss']:.3f} °C")
    ax.axhline(T_LIM, color="k", ls="--", lw=1, label="Límite 93 °C (fuera de escala: B no lo alcanza)")
    ax.set_ylim(14, 23)
    ax.set_xlabel("t [min]"); ax.set_ylabel("Temperatura máxima [°C]"); ax.set_title("Caso B: calentamiento (escala ampliada)")
    ax.grid(alpha=0.3); ax.legend(fontsize=7, loc="lower right")
    fig.suptitle("Prueba I: temperatura máxima frente al tiempo (T inicial = 15 °C, q'' = 150 W/m²)", fontsize=11)
    fig.tight_layout(); fig.savefig("calentamiento_modificado_v1.png", dpi=150); plt.close(fig)

    # --- 3. Calentamiento normalizado ---
    fig, axs = plt.subplots(1, 2, figsize=(12, 4.6))
    for ax, tmax_h in zip(axs, (None, 6.0)):
        for caso, col in (("A", colA), ("B", colB)):
            r = base[caso]["cal"]; Tss = base[caso]["Tmax_ss"]
            frac = (r["hist"].max(axis=1) - T_I_CAL) / (Tss - T_I_CAL)
            ax.plot(r["hist_t"] / 3600, frac, color=col, label=f"{caso}, nodal explícito")
            cc = conc["A_sin"] if caso == "A" else conc["B"]
            tt = np.linspace(0, r["hist_t"][-1], 400)
            ax.plot(tt / 3600, 1 - np.exp(-tt / cc["tau"]), "--", color=col, alpha=0.6, label=f"{caso}, concentrado")
            ax.plot(r["cruces"]["t95"] / 3600, FRAC, "o", color=col)
            ax.annotate(f"t95,{caso} = {r['cruces']['t95']/3600:.3f} h", (r["cruces"]["t95"] / 3600, FRAC),
                        textcoords="offset points", xytext=(6, -14) if caso == "B" else (-95, -16), fontsize=8)
        ax.axhline(FRAC, color="k", ls=":", lw=0.8)
        ax.set_xlabel("t [h]"); ax.set_ylabel("(T máx − Ti)/(T máx,ss − Ti)")
        ax.grid(alpha=0.3)
        if tmax_h:
            ax.set_xlim(0, tmax_h); ax.set_title("Ampliación 0–6 h")
        else:
            ax.set_title("Escala completa")
        ax.legend(fontsize=7, loc="lower right")
    fig.suptitle("Calentamiento normalizado: definición de t95 (cada caso respecto a su propio T máx,ss)", fontsize=11)
    fig.tight_layout(); fig.savefig("calentamiento_normalizado_modificado_v1.png", dpi=150); plt.close(fig)

    # --- 4. Enfriamiento ---
    fig, axs = plt.subplots(1, 2, figsize=(12, 4.8))
    for ax, ampl in zip(axs, (False, True)):
        for caso, col in (("A", colA), ("B", colB)):
            r = base[caso]["enf"]
            ax.plot(r["hist_t"] / 3600, r["hist"].max(axis=1), color=col, label=f"{caso}, nodal explícito (T máx)")
            cc = conc["A_sin"] if caso == "A" else conc["B"]
            tt = np.linspace(0, r["hist_t"][-1], 400)
            ax.plot(tt / 3600, cc["T_de_t_enf"](tt), "--", color=col, alpha=0.6, label=f"{caso}, concentrado")
            t60 = r["cruces"]["t_enf"] / 3600
            ax.plot(t60, T_OBJ_ENF, "o", color=col)
            ax.annotate(f"{caso}: {t60:.3f} h ({t60*60:.1f} min)", (t60, T_OBJ_ENF), textcoords="offset points",
                        xytext=(8, -16) if caso == "B" else (-130, -24), fontsize=8)
        ax.axhline(T_OBJ_ENF, color="k", ls="--", lw=1, label="Objetivo 60 °C")
        ax.set_xlabel("t [h]"); ax.set_ylabel("Temperatura máxima [°C]"); ax.grid(alpha=0.3)
        ax.set_ylim(55, 92)
        if ampl:
            ax.set_xlim(0, 1.0); ax.set_title("Ampliación: 0–1 h (caso B visible)")
        else:
            ax.set_title("Escala completa")
        ax.legend(fontsize=7, loc="center right" if ampl else "upper right")
    fig.suptitle("Prueba II: enfriamiento desde 90 °C uniforme (base adiabática, convección en la cara superior)", fontsize=11)
    fig.tight_layout(); fig.savefig("enfriamiento_modificado_v1.png", dpi=150); plt.close(fig)


if __name__ == "__main__":
    main()
