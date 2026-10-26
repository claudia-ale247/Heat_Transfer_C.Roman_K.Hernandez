# Proyecto de Transferencia de Calor — Ejercicio 5-34

**Estudiantes:**

- Karina Hernández Cruz
- Claudia Román García

Este proyecto presenta la solución del ejercicio original 5-34 y su adaptación para estudiar el comportamiento transitorio y evaluar una configuración que reduzca el tiempo de enfriamiento.

El repositorio reúne cálculos manuales, conversaciones con Claude, reportes, código de Python, gráficas, tablas de resultados y auditorías. Las versiones muestran cómo evolucionó el trabajo, qué observaciones se identificaron y cómo se incorporaron las correcciones.

## 1. Organización y estado del proyecto

| Parte | Contenido | Estado |
| --- | --- | --- |
| Ejercicio original | Solución estacionaria, cálculos manuales, tres versiones, conversaciones, código, gráficas y auditorías | Cuenta con un PDF de la versión 3 aprobado y firmado |
| Ejercicio modificado | Análisis transitorio de los casos A y B, comparación de calentamiento y enfriamiento, cálculos manuales y tres versiones | Cuenta con un PDF de la versión 3 aprobado y firmado |
| Comparación final | Evaluación de la mejora, interpretación y condiciones de validez | Documentada en este README y en los reportes |

### Documentos principales del ejercicio original

- [Reporte final aprobado y firmado](01_Ejercicio_original/Version_3/Reporte_original_v3_aprobado_y_firmado.pdf)
- [Auditoría del reporte 3](01_Ejercicio_original/Version_3/Auditoria_del_reporte_3.pdf)
- [Cálculos manuales](01_Ejercicio_original/Calculo_manual_Ejercicio_original_5_34.pdf)
- [Conversación completa con Claude](01_Ejercicio_original/Conversacion_completa_con_Claude.md)
- [Explorar el ejercicio original](01_Ejercicio_original/)

### Documentos principales del ejercicio modificado

- [Reporte final aprobado y firmado](02_Ejercicio_modificado/Version_3/Reporte_modificado_v3_aprobado_y_firmado.pdf)
- [Auditoría del reporte 3](02_Ejercicio_modificado/Version_3/Auditoria_del_reporte_modificado_3.pdf)
- [Cálculos manuales y tablas de Excel](02_Ejercicio_modificado/Calculos_manuales_Ejercicio_modificado_5_34.pdf)
- [Conversación completa con Claude](02_Ejercicio_modificado/Conversacion_completa_con_Claude.md)
- [Explorar el ejercicio modificado](02_Ejercicio_modificado/)

### Cómo se distinguen los documentos de la versión 3

Para ambos ejercicios se conservan documentos con funciones distintas:

| Documento | Función |
| --- | --- |
| Reporte en Markdown, Word y PDF sin firmas | Conserva la entrega técnica preparada para revisión, antes de la aprobación firmada |
| Reporte auditado | Documenta las observaciones y el cierre de la revisión |
| PDF aprobado y firmado | Registra la aprobación de ambas estudiantes y constituye la copia final de entrega |

**La aprobación y las firmas se documentan únicamente en el PDF identificado como aprobado y firmado.** Los reportes técnicos y la copia auditada pueden conservar expresiones correspondientes a su estado previo a la aprobación.

## 2. Ejercicio original 5-34

### 2.1. Objetivo y descripción

El ejercicio estudia la conducción unidimensional en estado estacionario a través de una pared compuesta por una placa metálica y una placa no metálica.

El calor entra por la base del metal, atraviesa ambas placas y sale por convección desde la superficie exterior hacia el aire.

Los objetivos son:

- Determinar las temperaturas de los 11 nodos mediante diferencias finitas.
- Representar gráficamente la distribución de temperatura.
- Evaluar si la temperatura máxima del metal cumple el límite de 93 °C indicado en el enunciado.
- Determinar el coeficiente de convección umbral y la condición necesaria para mantener el metal por debajo de ese límite.

| Dato | Valor |
| --- | --- |
| Conductividad del metal | 36 W/(m·K) |
| Espesor del metal | 30 mm |
| Conductividad del no metal | 0.05 W/(m·K) |
| Espesor del no metal | 20 mm |
| Flujo de calor entrante | 150 W/m² |
| Coeficiente de convección original | 5 W/(m²·K) |
| Temperatura del aire | 15 °C |
| Separación entre nodos | 5 mm |
| Límite de temperatura del metal | 93 °C |

### 2.2. Por qué se desarrollaron tres versiones

Las tres versiones documentan el proceso de generación, auditoría y corrección del reporte; no representan tres ejercicios diferentes.

#### Versión 1 — Reporte inicial y primera auditoría

El primer prompt produjo el reporte inicial, el código de Python y la gráfica de temperaturas.

La revisión identificó explicaciones que requerían mayor claridad sobre las suposiciones, los balances de energía, la interfaz entre materiales, las unidades y la notación. Las observaciones se registraron en la auditoría y sirvieron para preparar el segundo prompt.

Esta versión se conserva como evidencia de la primera entrega de Claude.

#### Versión 2 — Correcciones y segunda auditoría

La segunda versión incorporó las aclaraciones solicitadas.

La nueva auditoría identificó ajustes adicionales: corregir la descripción de la disminución de temperatura en el metal, precisar la explicación sobre los errores de punto flotante y actualizar el estado de la comparación manual.

Estos ajustes no requirieron cambiar las temperaturas nodales ni el coeficiente de convección umbral.

#### Versión 3 — Confirmación manual y cierre

La tercera versión incorporó las correcciones anteriores. Posteriormente, se actualizó dentro de esta misma versión el estado de las comprobaciones manuales confirmadas por las estudiantes.

**En las versiones 1 y 2 todavía no se había registrado la confirmación final de las comprobaciones manuales. Para la versión 3, Karina Hernández Cruz y Claudia Román García confirmamos la coincidencia de los cálculos revisados con nuestros cálculos manuales, considerando el redondeo.**

Esta confirmación corresponde al trabajo de las estudiantes y se distingue de las comprobaciones computacionales de Claude. No implica que Claude haya inspeccionado el documento manual del ejercicio original.

La revisión quedó documentada en la auditoría de la versión 3. La aprobación se registró por separado en el PDF firmado por ambas estudiantes.

Las versiones 1 y 2 permanecen disponibles como evidencia del proceso. La confirmación de los cálculos no modifica por sí sola el estado de revisión de las referencias a diapositivas, registrado por separado en la documentación.

### 2.3. Conversaciones con Claude

La conversación global reúne los prompts, las respuestas y los archivos entregados durante las tres versiones. También se conservan las conversaciones individuales dentro de cada carpeta.

| Registro | Acceso |
| --- | --- |
| Conversación global | [Leer conversación completa](01_Ejercicio_original/Conversacion_completa_con_Claude.md) |
| Conversación de la versión 1 | [Leer prompt 1 y respuestas](01_Ejercicio_original/Version_1/Conversaci%C3%B3n_con_Claude.md) |
| Conversación de la versión 2 | [Leer prompt 2 y respuestas](01_Ejercicio_original/Version_2/Conversacion_con_Claude.md) |
| Conversación de la versión 3 | [Leer prompt 3, actualización y respuestas](01_Ejercicio_original/Version_3/Conversacion_con_Claude.md) |

Las auditorías son documentos separados. Las observaciones enviadas a Claude para solicitar correcciones aparecen en los prompts correspondientes.

### 2.4. Archivos de la versión 1

Primera entrega del ejercicio original y su auditoría.

| Archivo | Acceso |
| --- | --- |
| Conversación con Claude | [Leer conversación](01_Ejercicio_original/Version_1/Conversaci%C3%B3n_con_Claude.md) |
| Reporte en PDF | [Leer reporte 1](01_Ejercicio_original/Version_1/Reporte_original_v1.pdf) |
| Reporte en Word | [Descargar documento editable](01_Ejercicio_original/Version_1/Reporte_original_v1.docx) |
| Reporte en Markdown | [Leer reporte](01_Ejercicio_original/Version_1/reporte_original_v1.md) |
| Código de Python | [Consultar código](01_Ejercicio_original/Version_1/ej_5_34_v1.py) |
| Gráfica de temperaturas | [Ver gráfica](01_Ejercicio_original/Version_1/T_vs_x_5_34_v1.png) |
| Auditoría del reporte 1 | [Leer auditoría](01_Ejercicio_original/Version_1/Auditoria_del_reporte_1.pdf) |

[Explorar la versión 1](01_Ejercicio_original/Version_1/)

### 2.5. Archivos de la versión 2

Segunda entrega y auditoría que dio lugar a los ajustes de la versión 3.

| Archivo | Acceso |
| --- | --- |
| Conversación con Claude | [Leer conversación](01_Ejercicio_original/Version_2/Conversacion_con_Claude.md) |
| Reporte en PDF | [Leer reporte 2](01_Ejercicio_original/Version_2/Reporte_original_v2.pdf) |
| Reporte en Word | [Descargar documento editable](01_Ejercicio_original/Version_2/Reporte_original_v2.docx) |
| Reporte en Markdown | [Leer reporte](01_Ejercicio_original/Version_2/reporte_original_v2.md) |
| Código de Python | [Consultar código](01_Ejercicio_original/Version_2/ej_5_34_v2.py) |
| Gráfica de temperaturas | [Ver gráfica](01_Ejercicio_original/Version_2/T_vs_x_5_34_v2.png) |
| Auditoría del reporte 2 | [Leer auditoría](01_Ejercicio_original/Version_2/Auditoria_del_reporte_2.pdf) |

[Explorar la versión 2](01_Ejercicio_original/Version_2/)

### 2.6. Archivos de la versión 3 — Cierre del ejercicio original

Se conservan la entrega técnica, la auditoría y la copia final aprobada y firmada.

| Archivo | Acceso |
| --- | --- |
| Conversación con Claude | [Leer conversación](01_Ejercicio_original/Version_3/Conversacion_con_Claude.md) |
| Reporte técnico en PDF, sin firmas | [Leer reporte 3](01_Ejercicio_original/Version_3/Reporte_original_v3.pdf) |
| Reporte técnico en Word | [Descargar documento editable](01_Ejercicio_original/Version_3/Reporte_original_v3.docx) |
| Reporte técnico en Markdown | [Leer reporte](01_Ejercicio_original/Version_3/reporte_original_v3.md) |
| Código de Python | [Consultar código](01_Ejercicio_original/Version_3/ej_5_34_v3.py) |
| Gráfica de temperaturas | [Ver gráfica](01_Ejercicio_original/Version_3/T_vs_x_5_34_v3.png) |
| Auditoría del reporte 3 | [Leer documento auditado](01_Ejercicio_original/Version_3/Auditoria_del_reporte_3.pdf) |
| PDF aprobado y firmado | [Leer entrega final](01_Ejercicio_original/Version_3/Reporte_original_v3_aprobado_y_firmado.pdf) |

El código y la gráfica se conservaron durante la actualización documental de esta versión, según lo registrado en la conversación.

[Explorar la versión 3](01_Ejercicio_original/Version_3/)

### 2.7. Comparación entre los cálculos manuales y el reporte de la versión 3

Las estudiantes resolvieron el ejercicio manualmente y contrastaron sus resultados con los del reporte generado con Claude.

[Consultar los cálculos manuales](01_Ejercicio_original/Calculo_manual_Ejercicio_original_5_34.pdf)

| Magnitud | Resultado manual | Reporte de Claude — Versión 3 | Comparación |
| --- | --- | --- | --- |
| T₀ — Base del metal | 105.125 °C | 105.125 °C | Coinciden |
| T₁ | 105.104 °C | 105.104 °C | Coinciden |
| T₂ | 105.083 °C | 105.083 °C | Coinciden |
| T₃ | 105.063 °C | 105.063 °C | Coinciden |
| T₄ | 105.042 °C | 105.042 °C | Coinciden |
| T₅ | 105.021 °C | 105.021 °C | Coinciden |
| T₆ — Interfaz | 105.000 °C | 105.000 °C | Coinciden |
| T₇ | 90.000 °C | 90.000 °C | Coinciden |
| T₈ | 75.000 °C | 75.000 °C | Coinciden |
| T₉ | 60.000 °C | 60.000 °C | Coinciden |
| T₁₀ — Superficie exterior | 45.000 °C | 45.000 °C | Coinciden |
| Coeficiente de convección umbral, h* | 8.392 W/(m²·K) | 8.392 W/(m²·K) | Coinciden |

Los resultados manuales coinciden con los del reporte. Las revisiones de las explicaciones, la notación y la presentación se encuentran en las auditorías.

**Nota:** Los valores de esta tabla se presentan a tres decimales. Los documentos de cálculo manual y del reporte de Claude conservan sus respectivos decimales originales.

### 2.8. Interpretación de los resultados

#### Distribución de temperatura

La temperatura disminuye desde la base del metal hasta la superficie expuesta al aire, en la dirección de transferencia del calor.

La temperatura máxima se encuentra en el nodo 0 y es de **105.125 °C**. En la interfaz es de **105 °C** y en la superficie exterior es de **45 °C**.

#### Diferencia entre los materiales

La caída de temperatura en el metal es de **0.125 °C**, mientras que en la placa no metálica es de **60 °C**.

La mayor caída ocurre en la placa no metálica porque su resistencia térmica a la conducción es mucho mayor. El perfil del metal parece casi horizontal en la gráfica general; la ampliación permite observar su pequeña disminución.

#### Evaluación del límite de 93 °C

El ejercicio requiere evaluar el límite térmico; no presupone que las condiciones originales deban cumplirlo.

Con **h = 5 W/(m²·K)**, la temperatura máxima supera el límite en **12.125 °C**. Por tanto, las condiciones originales no satisfacen el criterio térmico indicado.

#### Significado del coeficiente de convección umbral

El valor **h* = 1200/143 ≈ 8.391608 W/(m²·K)** produce una temperatura máxima de exactamente **93 °C**, manteniendo constantes los demás datos.

- **h = h*:** la temperatura máxima es igual a 93 °C.
- **h > h*:** la temperatura máxima es menor que 93 °C.

El valor 8.39 es una aproximación. Para establecer la condición estricta se conserva el valor exacto, ya que utilizar literalmente 8.39 produce una temperatura ligeramente superior a 93 °C.

#### Conclusión del ejercicio original

La solución manual y el reporte coinciden en las temperaturas nodales y el coeficiente de convección umbral.

Las condiciones originales producen una temperatura máxima superior al límite. Aumentar la convección por encima del umbral permite reducirla por debajo de 93 °C, manteniendo constantes los demás datos.

Las tres versiones documentan la revisión progresiva. El PDF aprobado y firmado de la versión 3 registra el cierre del ejercicio original.

## 3. Ejercicio modificado 5-34

### 3.1. Objetivo y descripción

Esta etapa extiende el ejercicio al régimen transitorio para calcular cómo cambia la temperatura con el tiempo y evaluar una configuración que enfríe más rápido.

Se estudian dos casos:

- **Caso A:** conserva la configuración original e incorpora el almacenamiento de energía para analizar su respuesta transitoria.
- **Caso B:** modifica el material de la capa superior, su espesor y el coeficiente de convección.

El análisis estacionario del ejercicio original permanece válido. La extensión transitoria responde preguntas adicionales sobre el tiempo necesario para calentar o enfriar el sistema.

| Parámetro | Caso A — Configuración original | Caso B — Configuración modificada |
| --- | --- | --- |
| Placa inferior | SB-96, 30 mm | SB-96, 30 mm |
| Conductividad de la placa inferior | 36 W/(m·K) | 36 W/(m·K) |
| Capa superior | Material no metálico | Aluminio |
| Espesor de la capa superior | 20 mm | 5 mm |
| Conductividad de la capa superior | 0.050 W/(m·K) | 237 W/(m·K) |
| Coeficiente de convección | 5 W/(m²·K) | 25 W/(m²·K) |
| Temperatura del aire | 15 °C | 15 °C |

La propuesta combina tres cambios. La mejora corresponde a esa combinación y no se atribuye únicamente al aluminio.

Las densidades, los calores específicos, las fuentes y los supuestos necesarios para calcular tiempos se documentan en el reporte.

#### Prueba de calentamiento

Ambos sistemas comienzan uniformemente a **15 °C** y reciben un flujo de calor de **150 W/m²** por la base.

Se estudian:

- La evolución de las temperaturas nodales.
- El cumplimiento del límite de 93 °C.
- El tiempo para completar el 95 % del aumento de temperatura de cada configuración.

#### Prueba de enfriamiento

Ambos sistemas comienzan uniformemente a **90 °C**, sin calentamiento y con la base adiabática. El aire permanece a **15 °C**.

Se compara el tiempo necesario para que la **temperatura máxima** disminuya hasta **60 °C**. Cada caso conserva sus materiales, espesores y coeficiente de convección.

Esta prueba permite comparar directamente el enfriamiento con temperaturas inicial y objetivo comunes.

### 3.2. Por qué se desarrollaron tres versiones

El ejercicio modificado tiene su propia numeración. Sus versiones documentan la revisión de esta segunda parte del proyecto.

#### Versión 1 — Desarrollo inicial y primera auditoría

El primer prompt produjo el planteamiento de los casos A y B, el reporte, el código, cuatro figuras y dos archivos CSV.

La auditoría revisó los cálculos, los métodos, los supuestos, las explicaciones y la atribución de las verificaciones. Las observaciones se utilizaron para preparar el segundo prompt.

Esta entrega se conserva como punto de partida del ejercicio modificado.

#### Versión 2 — Correcciones y segunda auditoría

La segunda versión incorporó las observaciones iniciales y precisó la comparación de los casos, las aproximaciones concentradas, el modelo nodal y las comprobaciones computacionales.

La revisión identificó la necesidad de completar la comparación documental y aclarar la procedencia de algunos valores, las diferencias numéricas y el alcance de cada comprobación.

Se distinguió la confirmación de las estudiantes de la comparación que Claude podía realizar con los documentos efectivamente disponibles en su sesión.

#### Versión 3 — Comparación documental y ajustes finales

Durante esta versión se incorporó el documento de cálculos de las estudiantes, incluidas sus tablas de Excel, y se actualizó la comparación con los resultados de Claude.

Se aclararon:

- Los valores procedentes del documento de las estudiantes.
- Los resultados obtenidos con el código.
- Las reconstrucciones computacionales utilizadas para explorar diferencias.
- Las definiciones del número de Biot.
- La procedencia de los tiempos y las diferencias de redondeo e interpolación.
- Los supuestos y el alcance de las comprobaciones.

Posteriormente, se ajustaron las menciones a la estructura propia de prompts autorizada por el profesor, la nota sobre Excel y la preparación de la copia para aprobación.

Estas actualizaciones se mantuvieron dentro de la versión 3; no se creó una versión 4.

**La auditoría registra el cierre de la revisión. La aprobación de Karina Hernández Cruz y Claudia Román García se documenta únicamente en el PDF aprobado y firmado.**

Los reportes en Markdown, Word y PDF sin firmas conservan su función como copias técnicas previas a la aprobación firmada.

Las respuestas históricas sobre archivos ausentes o verificaciones pendientes permanecen en la conversación para mostrar la secuencia del trabajo. Las actualizaciones posteriores documentan cómo avanzó la revisión.

### 3.3. Conversaciones con Claude

La conversación global reúne las tres versiones. Cada carpeta también conserva su conversación individual.

| Registro | Acceso |
| --- | --- |
| Conversación global | [Leer conversación completa](02_Ejercicio_modificado/Conversacion_completa_con_Claude.md) |
| Conversación de la versión 1 | [Leer prompt 1 y respuestas](02_Ejercicio_modificado/Version_1/Conversacion_con_Claude.md) |
| Conversación de la versión 2 | [Leer prompt 2 y respuestas](02_Ejercicio_modificado/Version_2/Conversacion_con_Claude.md) |
| Conversación de la versión 3 | [Leer prompt 3, aclaraciones y respuestas](02_Ejercicio_modificado/Version_3/Conversacion_con_Claude.md) |

Las conversaciones registran las solicitudes y las respuestas. Las auditorías y los documentos firmados se conservan por separado.

### 3.4. Archivos de la versión 1

Primera entrega del ejercicio modificado y su auditoría.

| Archivo | Acceso |
| --- | --- |
| Conversación con Claude | [Leer conversación](02_Ejercicio_modificado/Version_1/Conversacion_con_Claude.md) |
| Reporte en PDF | [Leer reporte 1](02_Ejercicio_modificado/Version_1/Reporte_modificado_v1.pdf) |
| Reporte en Word | [Descargar documento editable](02_Ejercicio_modificado/Version_1/Reporte_modificado_v1.docx) |
| Reporte en Markdown | [Leer reporte](02_Ejercicio_modificado/Version_1/reporte_modificado_v1.md) |
| Código de Python | [Consultar código](02_Ejercicio_modificado/Version_1/ej_5_34_modificado_v1.py) |
| Esquema de los casos A y B | [Ver esquema](02_Ejercicio_modificado/Version_1/esquema_casos_modificado_v1.png) |
| Gráfica de calentamiento | [Ver gráfica](02_Ejercicio_modificado/Version_1/calentamiento_modificado_v1.png) |
| Gráfica de calentamiento normalizado | [Ver gráfica](02_Ejercicio_modificado/Version_1/calentamiento_normalizado_modificado_v1.png) |
| Gráfica de enfriamiento | [Ver gráfica](02_Ejercicio_modificado/Version_1/enfriamiento_modificado_v1.png) |
| Resultados numéricos | [Consultar CSV](02_Ejercicio_modificado/Version_1/resultados_modificado_v1.csv) |
| Estudio de convergencia | [Consultar CSV](02_Ejercicio_modificado/Version_1/convergencia_modificado_v1.csv) |
| Auditoría del reporte 1 | [Leer auditoría](02_Ejercicio_modificado/Version_1/Auditoria_del_reporte_modificado_v1.pdf) |

[Explorar la versión 1](02_Ejercicio_modificado/Version_1/)

### 3.5. Archivos de la versión 2

Segunda entrega y auditoría utilizada para preparar los ajustes de la versión 3.

| Archivo | Acceso |
| --- | --- |
| Conversación con Claude | [Leer conversación](02_Ejercicio_modificado/Version_2/Conversacion_con_Claude.md) |
| Reporte en PDF | [Leer reporte 2](02_Ejercicio_modificado/Version_2/Reporte_modificado_v2.pdf) |
| Reporte en Word | [Descargar documento editable](02_Ejercicio_modificado/Version_2/Reporte_modificado_v2.docx) |
| Reporte en Markdown | [Leer reporte](02_Ejercicio_modificado/Version_2/reporte_modificado_v2.md) |
| Código de Python | [Consultar código](02_Ejercicio_modificado/Version_2/ej_5_34_modificado_v2.py) |
| Esquema de los casos A y B | [Ver esquema](02_Ejercicio_modificado/Version_2/esquema_casos_modificado_v2.png) |
| Gráfica de calentamiento | [Ver gráfica](02_Ejercicio_modificado/Version_2/calentamiento_modificado_v2.png) |
| Gráfica de calentamiento normalizado | [Ver gráfica](02_Ejercicio_modificado/Version_2/calentamiento_normalizado_modificado_v2.png) |
| Gráfica de enfriamiento | [Ver gráfica](02_Ejercicio_modificado/Version_2/enfriamiento_modificado_v2.png) |
| Resultados numéricos | [Consultar CSV](02_Ejercicio_modificado/Version_2/resultados_modificado_v2.csv) |
| Estudio de convergencia | [Consultar CSV](02_Ejercicio_modificado/Version_2/convergencia_modificado_v2.csv) |
| Auditoría del reporte 2 | [Leer auditoría](02_Ejercicio_modificado/Version_2/Auditoria_del_reporte_modificado_v2.pdf) |

[Explorar la versión 2](02_Ejercicio_modificado/Version_2/)

### 3.6. Archivos de la versión 3 — Cierre del ejercicio modificado

Se conservan la entrega técnica, los archivos de cálculo, la auditoría y el PDF aprobado y firmado.

| Archivo | Acceso |
| --- | --- |
| Conversación con Claude | [Leer conversación](02_Ejercicio_modificado/Version_3/Conversacion_con_Claude.md) |
| Reporte técnico en PDF, sin firmas | [Leer reporte 3](02_Ejercicio_modificado/Version_3/Reporte_modificado_v3.pdf) |
| Reporte técnico en Word | [Descargar documento editable](02_Ejercicio_modificado/Version_3/Reporte_modificado_v3.docx) |
| Reporte técnico en Markdown | [Leer reporte](02_Ejercicio_modificado/Version_3/reporte_modificado_v3.md) |
| Código de Python | [Consultar código](02_Ejercicio_modificado/Version_3/ej_5_34_modificado_v3.py) |
| Esquema de los casos A y B | [Ver esquema](02_Ejercicio_modificado/Version_3/esquema_casos_modificado_v3.png) |
| Gráfica de calentamiento | [Ver gráfica](02_Ejercicio_modificado/Version_3/calentamiento_modificado_v3.png) |
| Gráfica de calentamiento normalizado | [Ver gráfica](02_Ejercicio_modificado/Version_3/calentamiento_normalizado_modificado_v3.png) |
| Gráfica de enfriamiento | [Ver gráfica](02_Ejercicio_modificado/Version_3/enfriamiento_modificado_v3.png) |
| Resultados numéricos | [Consultar CSV](02_Ejercicio_modificado/Version_3/resultados_modificado_v3.csv) |
| Estudio de convergencia | [Consultar CSV](02_Ejercicio_modificado/Version_3/convergencia_modificado_v3.csv) |
| Auditoría del reporte 3 | [Leer documento auditado](02_Ejercicio_modificado/Version_3/Auditoria_del_reporte_modificado_3.pdf) |
| PDF aprobado y firmado | [Leer entrega final](02_Ejercicio_modificado/Version_3/Reporte_modificado_v3_aprobado_y_firmado.pdf) |

Según las respuestas de Claude, el código, las figuras y los CSV se conservaron durante las actualizaciones documentales finales de esta versión.

**El PDF aprobado y firmado es la copia de entrega.** Los demás formatos y el documento auditado conservan el registro de la etapa previa a esa aprobación.

[Explorar la versión 3](02_Ejercicio_modificado/Version_3/)

### 3.7. Comparación con los cálculos de las estudiantes

[Consultar los cálculos manuales y las tablas de Excel](02_Ejercicio_modificado/Calculos_manuales_Ejercicio_modificado_5_34.pdf)

El documento de las estudiantes incluye desarrollo manual y tablas obtenidas en Excel. La siguiente comparación resume el contraste documentado en el reporte de la versión 3.

| Magnitud | Documento de las estudiantes | Reporte de Claude — Versión 3 | Comparación |
| --- | --- | --- | --- |
| Tiempo nodal para alcanzar 93 °C, caso A | 33.083 h | 33.085 h | Diferencia documentada por coeficientes e interpolación |
| Constante de tiempo concentrada de B, incluyendo la resistencia del aluminio | 4379.430 s | 4379.970 s | Diferencia aproximada de 0.012 %, asociada al redondeo de U |
| Tiempo nodal de enfriamiento de A, 90→60 °C | 8.530 h | 8.536 h | Concordancia aproximada; se conserva la diferencia |
| Tiempo nodal de enfriamiento de B, 90→60 °C | 37.700 min | 37.770 min | Concordancia aproximada; se conserva la diferencia |
| Factor de tiempos de enfriamiento, tA/tB | 13.580 | 13.560 | Calculado con tiempos de distinta precisión |

**Nota:** Los valores se presentan a tres decimales. Añadir ceros no aumenta la precisión de los valores originales; los documentos conservan sus respectivas cifras y explicaciones.

#### Interpretación de las diferencias

El tiempo de **33.0825 h** del documento de las estudiantes se obtuvo mediante interpolación entre filas separadas 15 h. El código utiliza pasos de 1 s para el caso A y obtiene aproximadamente **33.085 h**.

La cercanía de estos resultados no representa una igualdad exacta. El reporte explica la influencia de la interpolación y de los coeficientes redondeados.

Las tablas de calentamiento de A presentan diferencias de hasta aproximadamente **0.026 °C**. Claude exploró su origen mediante una reconstrucción con coeficientes redondeados y presentó esa explicación como inferida. Los resultados de esa reconstrucción se distinguen de los valores escritos en el documento de las estudiantes.

La comparación abarcó los cálculos manuales y los valores de Excel incluidos en el PDF; no incluyó la inspección de las fórmulas internas del archivo Excel.

Las comprobaciones computacionales adicionales se identifican por separado. No se atribuyen a las estudiantes cálculos que no aparecen en su documento.

### 3.8. Interpretación de los resultados

#### Temperaturas y límite térmico

Con calentamiento de **150 W/m²**, las temperaturas máximas estacionarias son:

- **Caso A:** 105.125 °C.
- **Caso B:** 21.128 °C.

El caso A alcanza **93 °C** aproximadamente a las **33.085 h**.

El caso B no alcanza ese límite bajo las condiciones de calentamiento estudiadas, pues su temperatura máxima estacionaria permanece por debajo de 93 °C.

#### Mejora del enfriamiento

Para disminuir la temperatura máxima de **90 a 60 °C**:

- **Caso A:** aproximadamente 8.536 h.
- **Caso B:** aproximadamente 37.770 min.

La reducción calculada con los tiempos sin redondear es de aproximadamente **92.625 %**, equivalente a un factor de tiempos de **13.560**.

Esta conclusión procede del cálculo transitorio de los tiempos de enfriamiento bajo temperaturas inicial y objetivo comunes.

#### Qué explica la mejora

La capa de aluminio más delgada reduce la resistencia a la conducción. El aumento del coeficiente de convección facilita la transferencia de calor hacia el aire.

También cambia la capacidad térmica del sistema. Por eso se comparan tiempos entre temperaturas comunes, sin suponer que ambos casos deben liberar exactamente la misma cantidad de energía.

La mejora corresponde a la combinación del cambio de material, la reducción de espesor y el aumento de convección.

#### Qué significa el tiempo de calentamiento normalizado

El tiempo para completar el 95 % del aumento de temperatura describe la aproximación relativa de cada sistema a su propio estado estacionario.

Como A y B tienen temperaturas finales distintas, esa comparación no equivale a medir el calentamiento hacia una misma temperatura absoluta.

#### Alcance de las conclusiones

Los resultados corresponden al modelo unidimensional, las propiedades constantes, las condiciones de frontera y los supuestos documentados.

El modelo concentrado se utiliza como aproximación y se distingue de la solución nodal, que representa la distribución espacial de temperatura.

El valor **h = 25 W/(m²·K)** es una condición adoptada para el caso B. Una implementación física debe proporcionar esa convección y comprobar las propiedades y condiciones de operación consideradas.

El cumplimiento del criterio térmico de **93 °C** del ejercicio no constituye una certificación integral de cumplimiento con ASME.

#### Conclusión del ejercicio modificado

La configuración B mantiene una temperatura máxima inferior al límite del ejercicio durante el calentamiento estudiado y reduce el tiempo de enfriamiento en la prueba comparativa.

La revisión conserva las diferencias numéricas reales y distingue los cálculos de las estudiantes de las comprobaciones computacionales adicionales.

El PDF aprobado y firmado de la versión 3 documenta la aprobación del reporte con los supuestos y el alcance de verificación descritos.

## 4. Comparación final del proyecto

| Aspecto | Configuración original / caso A | Caso B modificado |
| --- | --- | --- |
| Capa superior | No metálica, 20 mm | Aluminio, 5 mm |
| Coeficiente de convección | 5 W/(m²·K) | 25 W/(m²·K) |
| Temperatura máxima estacionaria con 150 W/m² | 105.125 °C | 21.128 °C |
| Criterio térmico de 93 °C | Las condiciones originales lo superan | Permanece por debajo durante el calentamiento estudiado |
| Enfriamiento de 90 a 60 °C, calculado mediante el análisis transitorio | 8.536 h | 37.770 min |
| Reducción del tiempo de enfriamiento frente al caso A | Referencia | Aproximadamente 92.625 % |

El ejercicio original establece la distribución de temperatura en estado estacionario.

Su extensión transitoria, denominada caso A, permite comparar tiempos con el caso B. Los tiempos de calentamiento y enfriamiento pertenecen a esta extensión y no se obtienen de la solución estacionaria por sí sola.

La mejora se sustenta en la comparación de tiempos bajo condiciones comunes, además de la reducción de la temperatura estacionaria.

## 5. Uso de inteligencia artificial y auditoría

Claude se utilizó como herramienta de apoyo para generar reportes, código, gráficas y documentos. ChatGPT se utilizó como apoyo para organizar el proyecto, preparar prompts y revisar el planteamiento y los resultados.

Las estudiantes utilizaron una estructura propia de prompts, conforme a la alternativa autorizada por el profesor.

Las auditorías evaluaron:

- Los cálculos, las unidades y la notación.
- La coherencia entre ecuaciones, tablas, código, gráficas y conclusiones.
- Los supuestos y los límites de los métodos empleados.
- Las explicaciones incompletas o que requerían aclaración.
- La terminología y su relación con el material discutido en clase.
- La procedencia de los valores.
- Las afirmaciones que requerían evidencia o corrección.
- La distinción entre cálculos manuales, resultados de Excel y comprobaciones computacionales adicionales.

Las conversaciones muestran las solicitudes y respuestas. Las auditorías documentan las observaciones. Los documentos de cálculo permiten contrastar los resultados.

**Ambos ejercicios conservan tres versiones. La aprobación final de cada uno se registra exclusivamente en su PDF aprobado y firmado por Karina Hernández Cruz y Claudia Román García.**
