# Ejercicio 5-34: conducción unidimensional estacionaria en una pared compuesta (diferencias finitas)

**Versión:** v1 (informe original)
**Archivos:** `reporte_original_v1.md`, `ej_5_34_v1.py`, `T_vs_x_5_34_v1.png`

## Material de referencia consultado

| Archivo | Páginas del PDF consultadas | Uso |
|---|---|---|
| `092126 2.pdf` | pág. 1 (instrucciones y rúbrica), pág. 2 (enunciado del 5-34, pág. 368 del libro), pág. 3 (Figura P5-34) | Datos, preguntas y numeración de nodos |
| `Libreta.pdf` | págs. 11–12 (sección 5-3, diapositivas 13–20) | Balance de energía en un elemento de volumen, nodo interior, fronteras con flujo especificado y convección, interfaz con contacto perfecto |
| `Libreta Examen 2.pdf` | págs. 2–3 (sección 3-1, diapositivas 5–11) | Concepto de resistencia térmica, resistencia de convección, red de resistencias, caída de temperatura ΔT = QR y paredes multicapa |

**No consultado:** la plantilla de prompts del GitHub de la clase (no estaba adjunta) ni `Libreta Heat Transfer examen .pdf`. La estructura de este informe sigue las partes A–H del prompt y no una plantilla de la clase. Las referencias a diapositivas indican el número de diapositiva impreso en cada archivo (cuatro por página del PDF).

---

## A. Objetivo y descripción del sistema

**Objetivo.** Determinar la temperatura en los 11 nodos de una pared compuesta mediante diferencias finitas, graficar T(x), evaluar si el metal cumple el límite de 93 °C del enunciado y hallar el coeficiente de convección $h$ umbral.

**Sistema.** Una placa de cobre-silicio ASME SB-96 (metal, 30 mm) soporta sobre su superficie superior una placa no metálica (20 mm). Por la superficie 1 (inferior del metal) entra un flujo de calor uniforme. El calor viaja en la dirección $+x$ por el metal y el no metal, y sale por convección desde la superficie 2 (superior del no metal) hacia el aire.

**Incógnitas.** Las temperaturas nodales $T_0, T_1, \dots, T_{10}$.

**Flujo y tasa.** El flujo de calor $q''$ se mide en W/m². La tasa de transferencia de calor es $\dot Q = q'' A$, en W. Como $A$ es la misma en toda la pared, se cancela en cada balance.

### Datos (verificados contra el enunciado y la Figura P5-34)

| Dato | Símbolo | Valor | Unidad |
|---|---|---|---|
| Conductividad del metal (SB-96) | $k_m$ | 36 | W/(m·K) |
| Espesor del metal | $L_m$ | 0.030 | m |
| Conductividad del no metal | $k_n$ | 0.05 | W/(m·K) |
| Espesor del no metal | $L_n$ | 0.020 | m |
| Flujo de calor entrante en la superficie 1 | $q''$ | 150 | W/m² |
| Coeficiente de convección en la superficie 2 | $h$ | 5 | W/(m²·K) |
| Temperatura del aire | $T_\infty$ | 15 | °C |
| Espaciamiento nodal | $\Delta x$ | 0.005 | m |
| Límite de temperatura de la placa SB-96 | $T_{lim}$ | 93 | °C |

**Verificación de datos.** Todos los valores coinciden con el enunciado (págs. 2–3 del PDF). El enunciado da los espesores como 20 mm (no metal) y 30 mm (SB-96), respectivamente. Con $\Delta x = 5$ mm resultan 6 intervalos en el metal y 4 en el no metal, es decir 11 nodos, consistente con la Figura P5-34 (nodos 0 a 10, interfaz en el nodo 6). No se encontraron discrepancias.

El enunciado pide: la temperatura en cada nodo, la gráfica de T(x), si el uso de la placa SB-96 cumple el límite de 93 °C y el menor valor de $h$ para que la placa quede por debajo de 93 °C.

---

## B. Suposiciones

**Condiciones dadas por el enunciado:** flujo uniforme de 150 W/m² en la superficie 1, convección en la superficie 2 con $T_\infty = 15$ °C y $h = 5$ W/(m²·K), espesores, conductividades, $\Delta x$ y límite de 93 °C.

**Suposiciones adoptadas:**

| Suposición | Justificación y efecto en los balances |
|---|---|
| Estado estacionario | El enunciado no lo dice de forma explícita. Es una interpretación consistente con los datos: da un flujo y una convección constantes y compara con un límite de temperatura, pero no da densidad, calor específico, condición inicial ni tiempos. La energía almacenada no cambia, así que $\Delta E_{elemento}/\Delta t = 0$. Las diferencias finitas aquí discretizan solo el espacio, por lo que usarlas no vuelve el problema transitorio. |
| Conducción unidimensional | Los efectos laterales se suponen despreciables, por lo que $T = T(x)$. La temperatura es uniforme en cada plano perpendicular a $x$, pero no es uniforme a través del espesor: varía con $x$. |
| Conductividad constante en cada material | Se usan los valores dados, $k_m$ y $k_n$. No se presentan datos que validen esta aproximación en el intervalo de temperaturas del problema. |
| Sin generación interna | El calor se aplica en una frontera, no dentro del material: $\dot e_{gen} = 0$. |
| Contacto térmico perfecto | No hay resistencia de contacto en la interfaz: la temperatura es continua y el flujo se conserva. |
| Radiación despreciable | El enunciado solo da un coeficiente de convección $h$, que en este modelo es exclusivamente convectivo. No se añade ningún término radiativo. |

---

## C. Distribución de los nodos

La coordenada $x$ parte de la superficie 1 (inferior del metal) hacia la superficie 2 (superior del no metal), con $\Delta x = 0.005$ m.

| Nodo | $x$ (mm) | Ubicación | Condición |
|---|---|---|---|
| 0 | 0 | Superficie 1 (frontera, metal) | Flujo de calor impuesto |
| 1–5 | 5–25 | Interior del metal | Balance de energía interior |
| 6 | 30 | Interfaz metal/no metal | Contacto perfecto |
| 7–9 | 35–45 | Interior del no metal | Balance de energía interior |
| 10 | 50 | Superficie 2 (frontera, no metal) | Convección |

---

## D. Formulación por diferencias finitas

### Balance general de energía (Libreta.pdf, pág. 11, diapositiva 13)

Para el elemento de volumen alrededor de un nodo:

$$\dot Q_{izq} + \dot Q_{der} + \dot E_{gen,elem} = \frac{\Delta E_{elem}}{\Delta t}$$

Al aplicar las suposiciones: $\dot E_{gen,elem} = \dot e_{gen}\,V_{elem} = 0$ (sin generación) y $\Delta E_{elem}/\Delta t = 0$ (estacionario). Queda

$$\sum \dot Q_{entra} = 0$$

Con $\dot Q = q'' A$, el área $A$ es común a todos los términos y se cancela, de modo que cada ecuación es un balance de flujos en W/m².

### Convención de signos y distancias

Cada término de conducción se escribe como entrada positiva al nodo:

$$q''_{vecino \to nodo} = k\,\frac{T_{vecino} - T_{nodo}}{\Delta x}$$

Esto es solo una convención de contabilidad. Si el valor resulta negativo, el calor físico sale del nodo hacia ese vecino. Con la coordenada definida, el calor físico va siempre en $+x$ porque $T$ disminuye al aumentar $x$.

**Ancho del volumen frente a distancia entre nodos.** El volumen de control de un nodo interior tiene ancho $\Delta x$. El de un nodo de frontera tiene ancho $\Delta x/2$, porque se extiende solo hacia el interior del material (Libreta.pdf, págs. 11–12, diapositivas 13, 16 y 17). Aun así, la conducción entre un nodo de frontera y su vecino se calcula con la distancia $\Delta x$ entre nodos. Como $\dot e_{gen} = 0$ y el régimen es estacionario, el ancho del volumen no aparece en las ecuaciones finales.

### Nodo 0: frontera con flujo impuesto (diapositiva 17)

$$q'' + k_m\,\frac{T_1 - T_0}{\Delta x} = 0$$

### Nodo interior del metal, $i = 1, \dots, 5$ (diapositiva 14)

$$k_m\,\frac{T_{i-1} - T_i}{\Delta x} + k_m\,\frac{T_{i+1} - T_i}{\Delta x} = 0 \;\;\Longrightarrow\;\; T_{i-1} - 2T_i + T_{i+1} = 0$$

### Nodo interior del no metal, $i = 7, 8, 9$ (diapositiva 14)

$$k_n\,\frac{T_{i-1} - T_i}{\Delta x} + k_n\,\frac{T_{i+1} - T_i}{\Delta x} = 0 \;\;\Longrightarrow\;\; T_{i-1} - 2T_i + T_{i+1} = 0$$

### Nodo 6: interfaz con contacto perfecto (diapositiva 20, ecuación 5-29)

$$k_m\,\frac{T_5 - T_6}{\Delta x} + k_n\,\frac{T_7 - T_6}{\Delta x} = 0$$

Ambos términos están escritos como entradas positivas al nodo. Físicamente, el calor llega desde el metal ($T_5 > T_6$) y sale hacia el no metal ($T_6 > T_7$), por lo que el segundo término es negativo y la suma da cero. Cada lado conserva su propia conductividad.

Con contacto perfecto, la temperatura es continua en la unión y el flujo se conserva, porque el volumen de control de la interfaz no almacena energía ni genera calor. Despejando:

$$T_6 = \frac{k_m T_5 + k_n T_7}{k_m + k_n}$$

Es un promedio ponderado por las conductividades, no un promedio aritmético simple. Los pesos son $36/36.05 \approx 99.86\,\%$ para $T_5$ y $0.05/36.05 \approx 0.14\,\%$ para $T_7$.

### Nodo 10: frontera con convección (diapositiva 18)

$$k_n\,\frac{T_9 - T_{10}}{\Delta x} + h\,(T_\infty - T_{10}) = 0$$

---

## E. Solución

### Las 11 ecuaciones

Con $k_m/\Delta x = 36/0.005 = 7200$ W/(m²·K) y $k_n/\Delta x = 0.05/0.005 = 10$ W/(m²·K).

**Cómo recuperar los coeficientes dimensionales.** Las ecuaciones interiores en temperatura ($T_{i-1} - 2T_i + T_{i+1} = 0$) se multiplican por $k/\Delta x$ para convertirlas en balances de flujo en W/m². Los residuos de la sección H se evalúan con esta forma.

| # | Nodo | Balance de flujo (W/m²) |
|---|---|---|
| 1 | 0 | $-7200\,T_0 + 7200\,T_1 = -150$ |
| 2 | 1 | $7200\,T_0 - 14400\,T_1 + 7200\,T_2 = 0$ |
| 3 | 2 | $7200\,T_1 - 14400\,T_2 + 7200\,T_3 = 0$ |
| 4 | 3 | $7200\,T_2 - 14400\,T_3 + 7200\,T_4 = 0$ |
| 5 | 4 | $7200\,T_3 - 14400\,T_4 + 7200\,T_5 = 0$ |
| 6 | 5 | $7200\,T_4 - 14400\,T_5 + 7200\,T_6 = 0$ |
| 7 | 6 | $7200\,T_5 - 7210\,T_6 + 10\,T_7 = 0$ |
| 8 | 7 | $10\,T_6 - 20\,T_7 + 10\,T_8 = 0$ |
| 9 | 8 | $10\,T_7 - 20\,T_8 + 10\,T_9 = 0$ |
| 10 | 9 | $10\,T_8 - 20\,T_9 + 10\,T_{10} = 0$ |
| 11 | 10 | $10\,T_9 - 15\,T_{10} = -75$ |

La ecuación 11 sale de $10(T_9 - T_{10}) + 5(15 - T_{10}) = 0$, es decir $10T_9 - 15T_{10} = -75$.

### Procedimiento algebraico a mano

1. Ec. 1: $T_0 - T_1 = 150/7200 = 1/48$ K.
2. Ec. 2 (nodo 1): $T_0 - T_1 = T_1 - T_2$, así que $T_1 - T_2 = 1/48$ K. Lo mismo en los nodos 2, 3 y 4: $T_2 - T_3 = T_3 - T_4 = T_4 - T_5 = 1/48$ K.
3. Ec. 6 (nodo 5): $7200(T_4 - T_5) = 7200(T_5 - T_6)$. Como $T_4 - T_5 = 1/48$, resulta $T_5 - T_6 = 1/48$ K.
4. Entonces $T_0 - T_6 = 6 \times \tfrac{1}{48} = 0.125$ K, es decir $T_6 = T_0 - 0.125$.
5. Ec. 7 (interfaz): $7200(T_5 - T_6) = 10(T_6 - T_7)$. Con $T_5 - T_6 = 1/48$: $150 = 10(T_6 - T_7)$, así que $T_6 - T_7 = 15$ K.
6. Ecs. 8 a 10: $T_6 - T_7 = T_7 - T_8 = T_8 - T_9 = T_9 - T_{10} = 15$ K. Por tanto $T_{10} = T_6 - 60$.
7. Ec. 11 con $T_9 = T_{10} + 15$: $10(T_{10} + 15) - 15\,T_{10} = -75 \Rightarrow 150 - 5\,T_{10} = -75 \Rightarrow T_{10} = 45$ °C.
8. Hacia atrás: $T_6 = 45 + 60 = 105$ °C y $T_0 = 105 + 0.125 = 105.125$ °C. Los demás nodos salen de sumar $1/48$ K por nodo en el metal y 15 K por nodo en el no metal.

### Solución con Python

`ej_5_34_v1.py` ensambla la matriz $A$ y el vector $b$ de la tabla anterior (balances en W/m²) y resuelve $A\,\mathbf T = \mathbf b$ con `numpy.linalg.solve`.

**Ejecución:**

```bash
pip install numpy matplotlib
python3 ej_5_34_v1.py
```

Bibliotecas: `numpy`, `matplotlib` y `fractions` (incluida en Python). El script imprime las temperaturas, flujos, residuos, la comparación con resistencias y el análisis de $h$, y guarda `T_vs_x_5_34_v1.png`.

---

## F. Resultados e interpretación

### Temperaturas (resultado real de la ejecución, redondeado a 4 decimales)

| Nodo | $x$ (mm) | Zona | $T$ (°C) |
|---|---|---|---|
| 0 | 0 | Frontera, flujo impuesto | 105.1250 |
| 1 | 5 | Metal | 105.1042 |
| 2 | 10 | Metal | 105.0833 |
| 3 | 15 | Metal | 105.0625 |
| 4 | 20 | Metal | 105.0417 |
| 5 | 25 | Metal | 105.0208 |
| 6 | 30 | Interfaz | 105.0000 |
| 7 | 35 | No metal | 90.0000 |
| 8 | 40 | No metal | 75.0000 |
| 9 | 45 | No metal | 60.0000 |
| 10 | 50 | Frontera, convección | 45.0000 |

### Gráfica

![T(x)](T_vs_x_5_34_v1.png)

La gráfica muestra T (°C) frente a $x$ (mm), con el metal y el no metal sombreados, la interfaz en $x = 30$ mm, el límite de 93 °C y una ampliación del perfil dentro del metal.

### Pendientes (ley de Fourier)

Con $q'' = -k\,\dfrac{dT}{dx}$ y $q'' = +150$ W/m² en la dirección $+x$:

- Metal: $\dfrac{dT}{dx} = -\dfrac{150}{36} = -4.1667$ K/m.
- No metal: $\dfrac{dT}{dx} = -\dfrac{150}{0.05} = -3000$ K/m.

Ambas son negativas porque $T$ disminuye al aumentar $x$. La pendiente del metal es pequeña, pero no es cero: suma 0.125 °C a lo largo de 30 mm, y sin ese gradiente no habría flujo de calor. La del no metal es 720 veces mayor, que es la razón $k_m/k_n$. En la ampliación del metal se ve esa caída lineal de 105.125 a 105.000 °C.

### Caídas de temperatura (resultado real de la ejecución)

| Tramo | $\Delta T$ (°C) | $R''$ (m²·K/W) |
|---|---|---|
| Dentro del metal ($T_0 - T_6$) | 0.125 | $8.333\times10^{-4}$ |
| Dentro del no metal ($T_6 - T_{10}$) | 60 | 0.4 |
| Superficie exterior − aire ($T_{10} - T_\infty$) | 30 | 0.2 |
| Total ($T_0 - T_\infty$) | 90.125 | 0.600833 |

Con el mismo flujo, la caída es proporcional a $R''$ (Libreta Examen 2.pdf, pág. 3, diapositiva 9). En el no metal, $R'' = L/k$ es unas 480 veces la del metal, por eso ahí se concentra la caída de los dos sólidos. Los 30 °C de la tercera fila son la diferencia entre la superficie exterior y el aire, no una caída dentro de un material. En la interfaz no hay salto de temperatura: $T_6 = 105$ °C desde ambos lados.

### Temperatura máxima y cumplimiento del límite

La temperatura máxima del metal es $T_0 = 105.125$ °C, en $x = 0$ (superficie 1). Excede el límite de 93 °C en 12.125 °C. Con el límite del enunciado, **el uso de la placa SB-96 en estas condiciones no cumpliría**. Esta conclusión es solo respecto al límite que da el ejercicio, no una certificación normativa del equipo.

---

## G. Coeficiente de convección requerido

La temperatura máxima, en función de $h$, es

$$T_0 = T_\infty + q''\left(\frac{1}{h} + \frac{L_n}{k_n} + \frac{L_m}{k_m}\right)$$

Con $T_0 = 93$ °C y los demás datos constantes:

1. $\dfrac{93 - 15}{150} = 0.52$ m²·K/W.
2. $\dfrac{1}{h} = 0.52 - 0.4 - 0.000833\ldots = \dfrac{143}{1200}$ m²·K/W $= 0.119167\ldots$ m²·K/W.
3. $h^* = \dfrac{1200}{143} = 8.391608\ldots$ W/(m²·K).

**Unidades:** todos los términos de $1/h$ están en m²·K/W, así que $h$ queda en W/(m²·K).

**Comprobación por sustitución** (resultado real de la ejecución, resolviendo el sistema completo):

| $h$ (W/(m²·K)) | $T_0$ (°C) | Respecto a 93 °C |
|---|---|---|
| $h^* = 8.391608\ldots$ | 93.000000 | Alcanza exactamente el límite |
| $h^* + 0.001$ | 92.997870 | Por debajo |
| 8.39 (redondeado hacia abajo) | 93.003427 | Por encima |
| 8.3916 | 93.000018 | Por encima |
| 8.5 | 92.772059 | Por debajo, margen de 0.227941 °C |

**Alcanzar exactamente 93 °C frente a mantenerse por debajo.** El valor $h^*$ produce exactamente 93 °C. Como $T_0$ disminuye al aumentar $h$, quedar estrictamente por debajo de 93 °C requiere

$$h > \frac{1200}{143} \approx 8.391608\;\text{W/(m²·K)}$$

Un valor redondeado hacia abajo, como 8.39, no cumple esa condición. Para $h = 8.5$ W/(m²·K), $T_0 = 92.772$ °C, por debajo del límite.

---

## H. Comprobaciones

### Definición de residuo

El residuo de una ecuación es el desequilibrio que queda al sustituir las temperaturas en ella. Aquí se calcula como $\mathbf r = A\,\mathbf T - \mathbf b$, con las ecuaciones expresadas como balances de flujo en W/m² (tabla de la sección E) y con las **temperaturas numéricas sin redondear** de `numpy.linalg.solve`.

### Residuos (resultado real de la ejecución)

| Nodo | Residuo (W/m²) |
|---|---|
| 0 a 8 | 0 |
| 9 | $1.421\times10^{-14}$ |
| 10 | $-2.842\times10^{-14}$ |
| Máximo en valor absoluto | $2.842\times10^{-14}$ |

Estos residuos indican que el solucionador resolvió el sistema que se le dio. No son prueba suficiente de que el planteamiento físico sea correcto, por eso se complementan con las comprobaciones siguientes.

### Solución independiente por resistencias térmicas (Libreta Examen 2.pdf, págs. 2–3, diapositivas 5–11)

Resistencias por unidad de área, $R''$ en m²·K/W:

- $R''_m = L_m/k_m = 8.333\times10^{-4}$
- $R''_n = L_n/k_n = 0.4$
- $R''_{conv} = 1/h = 0.2$

Las resistencias en K/W son $R = R''/A$, es decir $L/(kA)$ y $1/(hA)$. Aquí se trabaja por unidad de área.

Con $q'' = 150$ W/m² constante en toda la cadena:

- $T_{10} = 15 + 150(0.2) = 45$ °C
- $T_6 = 45 + 150(0.4) = 105$ °C
- $T_0 = 105 + 150(8.333\times10^{-4}) = 105.125$ °C

Comparando los 11 nodos (perfil lineal dentro de cada material) con la solución numérica, la diferencia máxima fue $5.726\times10^{-11}$ °C (resultado real de la ejecución). Es una diferencia de punto flotante, no un error de ecuaciones.

### Flujo en cada tramo (resultado real de la ejecución)

$q'' = k\,(T_i - T_{i+1})/\Delta x$ dio **150.000000000 W/m²** en los diez tramos, y el flujo convectivo $h\,(T_{10} - T_\infty)$ dio 150.000000000 W/m².

### Tabla de comprobaciones

| Resultado o ecuación | Método de comprobación | Resultado |
|---|---|---|
| Temperaturas nodales | Solución independiente por resistencias | Coinciden; diferencia máxima $5.726\times10^{-11}$ °C |
| Balance global | $q''_{in}$ frente a $h\,(T_{10} - T_\infty)$ | $150 = 5 \times 30 = 150$ W/m² |
| Flujo en cada tramo | $k\,(T_i - T_{i+1})/\Delta x$, 10 tramos | 150.000000000 W/m² en todos |
| Continuidad en la interfaz | Tramos 5→6 y 6→7 | 150.000000000 W/m² en ambos |
| Condición de frontera, nodo 0 | Residuo de la ec. 1 | 0 |
| Condición de frontera, nodo 10 | Residuo de la ec. 11 | $-2.842\times10^{-14}$ W/m² |
| Residuos de las 11 ecuaciones | $A\,\mathbf T - \mathbf b$ en W/m², $T$ sin redondear | Máximo $2.842\times10^{-14}$ W/m² |
| Coherencia física | Signo de las pendientes y unidades | $T$ baja con $x$; unidades consistentes |

### Efecto del redondeo

Si se verifica la ecuación de la interfaz con temperaturas redondeadas a 4 decimales, por ejemplo $T_5 = 105.0208$, resulta $7200(T_5 - 105) = 7200 \times 0.0208 = 149.76$ W/m² y no 150. Esa diferencia es de redondeo, no un error de las ecuaciones: con $T_5 - T_6 = 1/48$ exacto, $7200/48 = 150$ W/m².

---

## Información adicional para la etapa siguiente (sin desarrollar)

Para demostrar un calentamiento o enfriamiento más rápido se necesitará un análisis transitorio. Una temperatura estacionaria menor no implica un menor tiempo de enfriamiento. Faltarían: densidad $\rho$ y calor específico $c_p$ de cada capa (no están en el enunciado y no se inventan), la condición inicial, qué ocurre con el flujo de 150 W/m² durante el proceso y un criterio de tiempo (por ejemplo, llegar a una temperatura dada). Una temperatura inicial uniforme sería una condición nueva, no el perfil estacionario calculado aquí.

---

## Cálculos que deben contrastar con su solución manual

1. Los coeficientes $7200$, $7210$, $10$ y $15$, y los términos independientes $-150$ y $-75$.
2. Los pasos 1 a 8 del procedimiento algebraico, en especial $T_5 - T_6 = 1/48$ K y $T_6 - T_7 = 15$ K.
3. Las 11 temperaturas, con $T_0 = 105.125$ °C, $T_6 = 105$ °C y $T_{10} = 45$ °C.
4. Las pendientes $-4.1667$ K/m y $-3000$ K/m, con su signo.
5. Las tres caídas de temperatura: 0.125 °C, 60 °C y 30 °C.
6. El despeje de $h^* = 1200/143$ y la sustitución de $h = 8.5$ W/(m²·K).
7. La comprobación por resistencias: $R''_m$, $R''_n$, $R''_{conv}$ y las temperaturas resultantes.
8. El efecto del redondeo en la ecuación de la interfaz (149.76 frente a 150 W/m²).

## Comprobaciones pendientes

- Contraste con la solución manual de ustedes: **pendiente**. Este informe solo contiene verificaciones hechas con código y por resistencias.
- No se usó la plantilla de prompts del GitHub de la clase (no estaba adjunta).
- Las referencias a diapositivas deben confirmarse al abrir los archivos de clase.
