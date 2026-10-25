# Proyecto de Transferencia de Calor — Ejercicio 5-34

**Estudiantes:**

- Karina Hernández Cruz
- Claudia Román García

Este repositorio documenta la solución del ejercicio original 5-34 y el desarrollo de una adaptación para estudiar una mejora en el calentamiento o enfriamiento del sistema.

El trabajo integra cálculos manuales, reportes generados con Claude, código de Python, gráficas y auditorías. Se conservan los prompts, las respuestas y las distintas versiones para mostrar el proceso de revisión y corrección.

## 1. Organización del proyecto

El proyecto se divide en dos partes:

| Parte | Contenido | Estado de la documentación |
| --- | --- | --- |
| Ejercicio original | Solución en estado estacionario, comparación manual, tres versiones del reporte, auditorías y documento aprobado y firmado | Archivos incorporados |
| Ejercicio modificado | Adaptación del sistema, justificación, cálculos, demostración de la mejora y comparación con el original | Pendiente de incorporar |

Los resultados del ejercicio original y del modificado se presentarán por separado para distinguir sus datos, condiciones y conclusiones.

## 2. Ejercicio original 5-34

### 2.1. Objetivo

El ejercicio original estudia la conducción unidimensional en estado estacionario a través de una pared compuesta por una placa metálica y una placa no metálica.

Se busca:

- Determinar las temperaturas de los 11 nodos mediante diferencias finitas.
- Representar la distribución de temperatura.
- Evaluar si la temperatura máxima del metal cumple el límite de 93 °C indicado en el enunciado.
- Determinar el coeficiente de convección umbral y la condición necesaria para mantener el metal por debajo de ese límite.

[Explorar la carpeta del ejercicio original](01_Ejercicio_original/)

### 2.2. Documentos principales

| Documento | Acceso |
| --- | --- |
| Reporte final aprobado y firmado | [Leer documento firmado](01_Ejercicio_original/Version_3/Reporte_original_v3_aprobado_y_firmado.pdf) |
| Auditoría del reporte final | [Consultar auditoría de la versión 3](01_Ejercicio_original/Version_3/Auditoria_del_reporte_3.pdf) |
| Cálculos manuales del ejercicio original | [Consultar desarrollo manual](01_Ejercicio_original/Calculo_manual_Ejercicio_original_5_34.pdf) |
| Reporte final en PDF | [Leer reporte final de Claude](01_Ejercicio_original/Version_3/Reporte_original_v3.pdf) |
| Reporte final editable | [Descargar documento de Word](01_Ejercicio_original/Version_3/Reporte_original_v3.docx) |
| Conversación global con Claude | [Consultar las tres versiones de la conversación](01_Ejercicio_original/Conversacion_completa_con_Claude.md) |

**La versión 3 es la versión final del ejercicio original.** La copia aprobada y firmada documenta la aprobación de las estudiantes. Las versiones 1 y 2 se conservan como evidencia del proceso de revisión.

### 2.3. Proceso de trabajo y conversaciones

La documentación conserva la siguiente secuencia:

1. Solución manual del ejercicio original.
2. Prompt inicial y generación del reporte 1.
3. Primera auditoría y solicitud de correcciones.
4. Generación del reporte 2 y segunda auditoría.
5. Generación del reporte 3 y actualización de las comprobaciones manuales.
6. Auditoría final y aprobación mediante el documento firmado.

La conversación global reúne los prompts, las respuestas y los enlaces a los archivos entregados. Las conversaciones individuales también se conservan en cada carpeta.

| Conversación | Acceso |
| --- | --- |
| Conversación global | [Consultar registro completo](01_Ejercicio_original/Conversacion_completa_con_Claude.md) |
| Versión 1 | [Consultar prompt 1 y respuestas](01_Ejercicio_original/Version_1/Conversaci%C3%B3n_con_Claude.md) |
| Versión 2 | [Consultar prompt 2 y respuestas](01_Ejercicio_original/Version_2/Conversacion_con_Claude.md) |
| Versión 3 | [Consultar prompt 3, ajustes adicionales y respuestas](01_Ejercicio_original/Version_3/Conversacion_con_Claude.md) |

Las auditorías de las estudiantes se presentan por separado de las respuestas de Claude. Las observaciones enviadas a Claude se conservan en los prompts correspondientes.

### 2.4. Versión 1 — Reporte inicial y primera auditoría

Primera entrega del ejercicio original, conservada como evidencia del contenido generado antes de aplicar las correcciones.

| Archivo | Acceso |
| --- | --- |
| Conversación con Claude | [Leer conversación](01_Ejercicio_original/Version_1/Conversaci%C3%B3n_con_Claude.md) |
| Reporte en PDF | [Leer reporte 1](01_Ejercicio_original/Version_1/Reporte_original_v1.pdf) |
| Reporte en Word | [Descargar documento editable](01_Ejercicio_original/Version_1/Reporte_original_v1.docx) |
| Reporte en Markdown | [Leer reporte en Markdown](01_Ejercicio_original/Version_1/reporte_original_v1.md) |
| Código de Python | [Consultar código](01_Ejercicio_original/Version_1/ej_5_34_v1.py) |
| Gráfica de temperaturas | [Ver gráfica](01_Ejercicio_original/Version_1/T_vs_x_5_34_v1.png) |
| Auditoría del reporte 1 | [Leer documento con anotaciones](01_Ejercicio_original/Version_1/Auditoria_del_reporte_1.pdf) |

[Explorar la carpeta de la versión 1](01_Ejercicio_original/Version_1/)

### 2.5. Versión 2 — Reporte revisado y segunda auditoría

Segunda entrega, elaborada a partir de las observaciones de la primera auditoría. Incorpora aclaraciones sobre las suposiciones, los balances de energía, las condiciones de frontera, la interfaz, la notación y el redondeo.

La segunda auditoría documenta las observaciones utilizadas para solicitar los ajustes de la versión 3.

| Archivo | Acceso |
| --- | --- |
| Conversación con Claude | [Leer conversación](01_Ejercicio_original/Version_2/Conversacion_con_Claude.md) |
| Reporte en PDF | [Leer reporte 2](01_Ejercicio_original/Version_2/Reporte_original_v2.pdf) |
| Reporte en Word | [Descargar documento editable](01_Ejercicio_original/Version_2/Reporte_original_v2.docx) |
| Reporte en Markdown | [Leer reporte en Markdown](01_Ejercicio_original/Version_2/reporte_original_v2.md) |
| Código de Python | [Consultar código](01_Ejercicio_original/Version_2/ej_5_34_v2.py) |
| Gráfica de temperaturas | [Ver gráfica](01_Ejercicio_original/Version_2/T_vs_x_5_34_v2.png) |
| Auditoría del reporte 2 | [Leer documento con anotaciones](01_Ejercicio_original/Version_2/Auditoria_del_reporte_2.pdf) |

[Explorar la carpeta de la versión 2](01_Ejercicio_original/Version_2/)

### 2.6. Versión 3 — Reporte final, auditoría y aprobación

La versión 3 incorpora los ajustes solicitados después de la segunda auditoría:

- Corrección de la descripción de la disminución de temperatura en el metal.
- Aclaración de que las diferencias numéricas de punto flotante corresponden a la ejecución realizada.
- Actualización de las comprobaciones manuales confirmadas por las estudiantes.
- Distinción entre la verificación manual de las estudiantes y las comprobaciones computacionales de Claude.

Se realizó una actualización adicional dentro de esta misma versión para registrar la confirmación de los cálculos manuales, conservando la denominación de versión 3.

Los reportes en PDF, Word y Markdown corresponden a la última entrega actualizada. El código y la gráfica se conservaron de la primera entrega de esta versión, según lo registrado en la conversación.

| Archivo | Acceso |
| --- | --- |
| Conversación con Claude | [Leer prompt 3 y actualización posterior](01_Ejercicio_original/Version_3/Conversacion_con_Claude.md) |
| Reporte final en PDF | [Leer reporte 3](01_Ejercicio_original/Version_3/Reporte_original_v3.pdf) |
| Reporte final en Word | [Descargar documento editable](01_Ejercicio_original/Version_3/Reporte_original_v3.docx) |
| Reporte final en Markdown | [Leer reporte en Markdown](01_Ejercicio_original/Version_3/reporte_original_v3.md) |
| Código de Python | [Consultar código](01_Ejercicio_original/Version_3/ej_5_34_v3.py) |
| Gráfica de temperaturas | [Ver gráfica](01_Ejercicio_original/Version_3/T_vs_x_5_34_v3.png) |
| Auditoría del reporte 3 | [Leer documento auditado](01_Ejercicio_original/Version_3/Auditoria_del_reporte_3.pdf) |
| Reporte aprobado y firmado | [Leer documento final firmado](01_Ejercicio_original/Version_3/Reporte_original_v3_aprobado_y_firmado.pdf) |

El reporte generado, el documento auditado y la copia firmada se conservan por separado para distinguir la entrega de Claude, las anotaciones de revisión y la aprobación de las estudiantes.

[Explorar la carpeta de la versión 3](01_Ejercicio_original/Version_3/)

### 2.7. Comparación entre los cálculos manuales y el reporte final

Las estudiantes resolvieron el ejercicio manualmente y compararon sus resultados con los del reporte final generado con Claude. Todos los valores se presentan a tres decimales para utilizar el mismo formato de comparación.

[Consultar el documento de cálculos manuales](01_Ejercicio_original/Calculo_manual_Ejercicio_original_5_34.pdf)

| Magnitud | Resultado manual | Reporte final de Claude — Versión 3 | Comparación |
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

Los resultados obtenidos manualmente coinciden con los del reporte final generado con Claude. Las revisiones de las explicaciones, la notación y la presentación se encuentran en las auditorías.

**Nota:** Los valores de esta tabla se presentan a tres decimales. Los documentos de cálculo manual y del reporte de Claude conservan sus respectivos decimales originales.

### 2.8. Interpretación de los resultados del ejercicio original

**Distribución de temperaturas**

La temperatura disminuye desde la base del metal hasta la superficie expuesta al aire. Este comportamiento es consistente con el calor que entra por la base y sale por convección hacia el ambiente.

La temperatura máxima se encuentra en el nodo 0 y es de **105.125 °C**. En la interfaz entre los materiales es aproximadamente **105 °C**, y en la superficie exterior es de **45 °C**.

**Comportamiento de los materiales**

La caída de temperatura a través del metal es de **0.125 °C**, mientras que en la placa no metálica es de **60 °C**.

La mayor caída ocurre en la placa no metálica porque presenta una resistencia térmica a la conducción mucho mayor. El perfil dentro del metal parece casi horizontal en la gráfica general, pero su ampliación muestra que la temperatura sí disminuye.

**Evaluación del límite de 93 °C**

El ejercicio requiere determinar si la temperatura del metal cumple el límite indicado; no presupone que las condiciones originales deban cumplirlo.

Con **h = 5 W/(m²·K)**, la temperatura máxima es **105.125 °C**, por lo que supera el límite en **12.125 °C**. Las condiciones originales no satisfacen el criterio térmico del enunciado.

Esta conclusión se refiere al límite de temperatura proporcionado en el ejercicio.

**Significado del coeficiente de convección calculado**

El valor **h* = 1200/143 ≈ 8.391608 W/(m²·K)** es el umbral que produce una temperatura máxima de exactamente **93 °C**, manteniendo los demás datos constantes.

- Para alcanzar exactamente **93 °C**, se utiliza **h = h***.
- Para mantener el metal estrictamente por debajo de **93 °C**, se requiere **h > h***.

El valor **8.39** es una aproximación del umbral. Si se utiliza literalmente, produce una temperatura ligeramente superior a 93 °C; por eso se conserva el valor exacto al establecer la condición.

**Conclusión del ejercicio original**

La solución manual y el reporte final de Claude coinciden en las temperaturas nodales y el coeficiente de convección umbral, considerando el redondeo.

El análisis demuestra que las condiciones originales producen una temperatura máxima superior al límite indicado. Aumentar el coeficiente de convección por encima del umbral calculado permite reducir la temperatura máxima estacionaria por debajo de 93 °C.

Este resultado describe el estado estacionario. Por sí solo, no determina el tiempo necesario para calentar o enfriar el sistema.

## 3. Ejercicio modificado

**Estado: pendiente de incorporar al repositorio.**

Esta parte documentará la adaptación del ejercicio original y la demostración de una mejora en el calentamiento o enfriamiento.

### 3.1. Planteamiento y justificación

Se presentarán:

- El objetivo de la modificación.
- Los parámetros que cambian respecto al ejercicio original.
- Los datos y condiciones que se conservan.
- Las nuevas condiciones y suposiciones.
- La justificación física de la mejora propuesta.
- El criterio utilizado para evaluar el calentamiento o enfriamiento más rápido.

### 3.2. Documentación y versiones

Se incorporarán las conversaciones con Claude, los reportes, el código, las gráficas, los cálculos manuales y las auditorías correspondientes.

Cada versión conservará sus propios archivos. La versión final se identificará expresamente y se acompañará de su documento aprobado y firmado.

### 3.3. Comparación entre los cálculos manuales y los resultados de Claude

Se añadirá una tabla con los resultados obtenidos manualmente, los resultados del reporte final del ejercicio modificado y la explicación de cualquier diferencia.

Esta comparación se mantendrá separada de la correspondiente al ejercicio original.

### 3.4. Interpretación y conclusiones del ejercicio modificado

Se explicará qué significan los resultados, cómo afectan las modificaciones al comportamiento térmico y bajo qué condiciones se demuestra la mejora.

Los resultados y conclusiones se incorporarán después de realizar y revisar los cálculos.

## 4. Comparación entre el ejercicio original y el modificado

**Estado: pendiente de completar.**

La comparación final distinguirá entre:

- Los cambios en los datos, la geometría y las condiciones de frontera.
- Las diferencias en las temperaturas y el comportamiento térmico.
- La comparación de tiempos de calentamiento o enfriamiento bajo condiciones iniciales y criterios definidos.
- La mejora obtenida y las suposiciones bajo las cuales es válida.

Una disminución de la temperatura estacionaria no se utilizará, por sí sola, como demostración de un menor tiempo de enfriamiento.

## 5. Uso de inteligencia artificial y auditoría

Claude se utilizó como herramienta de apoyo para generar reportes, código, gráficas y documentos en distintos formatos.

Los prompts y las respuestas se conservan para documentar las solicitudes realizadas y los cambios entre versiones.

Las auditorías revisan:

- Los cálculos y sus unidades.
- La coherencia entre ecuaciones, tablas, gráficas y conclusiones.
- Las explicaciones incompletas o que requieren aclaración.
- La terminología y su relación con el material discutido en clase.
- Las afirmaciones y limitaciones de las comprobaciones realizadas.

La solución manual de las estudiantes se utiliza para contrastar los resultados de la AI. Las comprobaciones computacionales se distinguen de la verificación manual.

Las copias aprobadas y firmadas documentan la aprobación de las estudiantes para la versión final correspondiente a cada ejercicio.
