# Proyecto de Transferencia de Calor — Ejercicio 5-34

**Estudiantes:**

- Karina Hernández Cruz
- Claudia Román García

Este repositorio presenta la solución del ejercicio original 5-34 y documentará su adaptación para lograr un calentamiento o enfriamiento más rápido.

El proyecto integra cálculos manuales, reportes generados con Claude, código de Python, gráficas y auditorías. Se conservan las conversaciones y las distintas versiones para mostrar cómo se revisaron los resultados y se incorporaron las correcciones.

## 1. Organización del proyecto

| Parte | Contenido | Estado |
| --- | --- | --- |
| Ejercicio original | Solución manual, tres versiones del reporte, conversaciones con Claude, código, gráficas, auditorías y reporte firmado | Documentación incorporada |
| Ejercicio modificado | Planteamiento de la adaptación, cálculos, demostración de la mejora, auditorías y reporte final | Pendiente de incorporar |
| Comparación final | Evaluación de las diferencias entre el ejercicio original y el modificado | Pendiente de incorporar |

Los datos, resultados y conclusiones de cada ejercicio se presentan por separado.

## 2. Ejercicio original 5-34

### 2.1. Objetivo y descripción

El ejercicio original estudia la conducción unidimensional en estado estacionario a través de una pared compuesta por una placa metálica y una placa no metálica.

El calor entra por la base del metal, atraviesa ambas placas y sale por convección desde la superficie exterior hacia el aire.

Se busca:

- Determinar las temperaturas de los 11 nodos mediante diferencias finitas.
- Graficar la distribución de temperatura.
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

[Explorar la carpeta del ejercicio original](01_Ejercicio_original/)

### 2.2. Documentos principales

| Documento | Acceso |
| --- | --- |
| Reporte final aprobado y firmado | [Leer documento firmado](01_Ejercicio_original/Version_3/Reporte_original_v3_aprobado_y_firmado.pdf) |
| Auditoría del reporte final | [Consultar auditoría de la versión 3](01_Ejercicio_original/Version_3/Auditoria_del_reporte_3.pdf) |
| Cálculos manuales | [Consultar desarrollo manual](01_Ejercicio_original/Calculo_manual_Ejercicio_original_5_34.pdf) |
| Reporte final de Claude en PDF | [Leer reporte 3](01_Ejercicio_original/Version_3/Reporte_original_v3.pdf) |
| Reporte final editable | [Descargar documento de Word](01_Ejercicio_original/Version_3/Reporte_original_v3.docx) |
| Conversación global con Claude | [Consultar las conversaciones de las tres versiones](01_Ejercicio_original/Conversacion_completa_con_Claude.md) |

**La versión 3 corresponde al reporte final del ejercicio original. La copia aprobada y firmada es el documento de cierre de esta parte del proyecto.**

### 2.3. Proceso de trabajo y evolución de los reportes

El ejercicio original se documentó en tres versiones mediante un proceso de generación, auditoría y corrección. Las estudiantes resolvieron el ejercicio manualmente y utilizaron sus resultados para contrastar las temperaturas nodales y el coeficiente de convección calculados por Claude.

**Versión 1 — Generación y primera revisión**

El primer prompt produjo el reporte inicial, el código y la gráfica. La primera auditoría identificó explicaciones que requerían mayor claridad sobre las suposiciones, los balances de energía, la interfaz entre materiales, las unidades, la notación y el redondeo.

Los resultados numéricos principales eran consistentes con la solución manual. Las observaciones se utilizaron para preparar el segundo prompt y mejorar el desarrollo del reporte.

**Versión 2 — Correcciones y segunda revisión**

La segunda versión incorporó las aclaraciones solicitadas. Al revisarla nuevamente, se identificaron ajustes pendientes: corregir la descripción de la disminución de temperatura en el metal, precisar la explicación de los errores de punto flotante y actualizar la información sobre la comparación con los cálculos manuales.

Estas observaciones dieron origen al tercer prompt. No implicaron cambiar las temperaturas ni el coeficiente de convección obtenidos.

**Versión 3 — Revisión final y aprobación**

La tercera versión incorporó los ajustes de la segunda auditoría. Posteriormente, se actualizó dentro de esta misma versión el estado de las comprobaciones manuales confirmadas por las estudiantes.

La auditoría final confirmó que las correcciones solicitadas estaban incorporadas y no identificó nuevas correcciones técnicas en los aspectos revisados. Las temperaturas nodales y el coeficiente de convección coincidieron con la solución manual, considerando el redondeo.

Por ello, la **versión 3 se conserva como el reporte final completo del ejercicio original**. Las versiones anteriores permanecen disponibles para mostrar la evolución del trabajo.

La aprobación técnica se distingue de la confirmación de las referencias a diapositivas, que se conservó como pendiente en el registro de auditoría.

**Conversaciones y registro del proceso**

La conversación global reúne los prompts, las respuestas y los enlaces a los archivos entregados. Las conversaciones individuales también se conservan dentro de cada carpeta.

| Conversación | Acceso |
| --- | --- |
| Conversación global | [Consultar registro completo](01_Ejercicio_original/Conversacion_completa_con_Claude.md) |
| Versión 1 | [Consultar prompt 1 y respuestas](01_Ejercicio_original/Version_1/Conversaci%C3%B3n_con_Claude.md) |
| Versión 2 | [Consultar prompt 2 y respuestas](01_Ejercicio_original/Version_2/Conversacion_con_Claude.md) |
| Versión 3 | [Consultar prompt 3, ajustes adicionales y respuestas](01_Ejercicio_original/Version_3/Conversacion_con_Claude.md) |

Las auditorías de las estudiantes se presentan como documentos separados. Las observaciones enviadas posteriormente a Claude se conservan en los prompts correspondientes.

### 2.4. Archivos de la versión 1

Primera entrega del ejercicio original y documento de su primera auditoría.

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

### 2.5. Archivos de la versión 2

Segunda entrega del ejercicio original y documento de la auditoría que dio lugar a los ajustes de la versión 3.

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

### 2.6. Archivos de la versión 3 — Entrega final

Los reportes en PDF, Word y Markdown corresponden a la última entrega actualizada de la versión 3. El código y la gráfica se conservaron de la primera entrega de esta versión, según lo registrado en la conversación.

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

Estos documentos cumplen funciones distintas:

- **Reporte_original_v3.pdf:** contiene el reporte técnico completo de la última entrega de Claude.
- **Auditoria_del_reporte_3.pdf:** contiene la revisión y el comentario de cierre de auditoría.
- **Reporte_original_v3_aprobado_y_firmado.pdf:** contiene el reporte y la certificación firmada por ambas estudiantes; es la copia final aprobada para la entrega.

[Explorar la carpeta de la versión 3](01_Ejercicio_original/Version_3/)

### 2.7. Comparación entre los cálculos manuales y el reporte final

Las estudiantes resolvieron el ejercicio manualmente y compararon sus resultados con los del reporte final generado con Claude.

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

La temperatura disminuye desde la base del metal hasta la superficie expuesta al aire. Este comportamiento es consistente con el calor que entra por la base, atraviesa las placas y sale por convección hacia el ambiente.

La temperatura máxima se encuentra en el nodo 0 y es de **105.125 °C**. En la interfaz entre los materiales es aproximadamente **105 °C**, y en la superficie exterior es de **45 °C**.

**Comportamiento de los materiales**

La caída de temperatura a través del metal es de **0.125 °C**, mientras que en la placa no metálica es de **60 °C**.

La mayor caída ocurre en la placa no metálica porque su resistencia térmica a la conducción es mucho mayor. El perfil dentro del metal parece casi horizontal en la gráfica general, pero su ampliación permite observar la disminución de temperatura.

**Evaluación del límite de 93 °C**

El ejercicio requiere determinar si la temperatura del metal cumple el límite indicado; no presupone que las condiciones originales deban cumplirlo.

Con **h = 5 W/(m²·K)**, la temperatura máxima es **105.125 °C**, por lo que supera el límite en **12.125 °C**. Por tanto, las condiciones originales no satisfacen el criterio térmico del enunciado.

**Significado del coeficiente de convección calculado**

El valor **h* = 1200/143 ≈ 8.391608 W/(m²·K)** es el umbral que produce una temperatura máxima de exactamente **93 °C**, manteniendo los demás datos constantes.

- Para alcanzar exactamente **93 °C**, se utiliza **h = h***.
- Para mantener el metal estrictamente por debajo de **93 °C**, se requiere **h > h***.

El valor **8.39** es una aproximación del umbral. Si se utiliza literalmente, produce una temperatura ligeramente superior a 93 °C; por eso se conserva el valor exacto al establecer la condición.

**Conclusión del ejercicio original**

La solución manual y el reporte final de Claude coinciden en las temperaturas nodales y el coeficiente de convección umbral.

El análisis demuestra que las condiciones originales producen una temperatura máxima superior al límite indicado. Aumentar el coeficiente de convección por encima del umbral calculado permite reducir la temperatura máxima estacionaria por debajo de 93 °C, manteniendo los demás datos constantes.

Las tres versiones documentan la mejora progresiva de las explicaciones y la presentación del reporte, conservando los resultados numéricos correctos.

## 3. Ejercicio modificado

**Estado: pendiente de incorporar al repositorio.**

Esta parte documentará la adaptación del ejercicio original y la demostración de una mejora en el calentamiento o enfriamiento del sistema.

### 3.1. Planteamiento y justificación

Se presentarán:

- El objetivo de la modificación.
- Los parámetros que cambian respecto al ejercicio original.
- Los datos y condiciones que se conservan.
- Las nuevas condiciones y suposiciones.
- La justificación física de la mejora propuesta.
- El criterio utilizado para evaluar el calentamiento o enfriamiento más rápido.

### 3.2. Proceso de trabajo y versiones

Se registrará la evolución del ejercicio modificado mediante sus prompts, respuestas, reportes y auditorías.

Cada versión conservará sus archivos correspondientes. Se explicarán las observaciones identificadas, las correcciones solicitadas y la razón por la que se selecciona una versión final.

### 3.3. Documentos del ejercicio modificado

Se incorporarán:

- Conversación global y conversaciones individuales con Claude.
- Reportes en PDF, Word y Markdown.
- Código de Python.
- Gráficas.
- Cálculos manuales.
- Auditorías.
- Reporte final aprobado y firmado.

Los enlaces se añadirán cuando los archivos estén disponibles.

### 3.4. Comparación entre los cálculos manuales y el reporte final

Se presentará una tabla con los resultados obtenidos manualmente y los del reporte final de Claude.

La comparación se mantendrá separada de la correspondiente al ejercicio original e incluirá las magnitudes utilizadas para demostrar la mejora propuesta.

### 3.5. Interpretación y conclusiones

Se explicará qué significan los resultados, cómo afectan las modificaciones al comportamiento térmico y bajo qué condiciones se demuestra la mejora.

Los resultados y conclusiones se incorporarán después de realizar y revisar los cálculos.

## 4. Comparación entre el ejercicio original y el modificado

**Estado: pendiente de completar.**

La comparación final presentará:

- Las diferencias en los parámetros y las condiciones de ambos ejercicios.
- El efecto de las modificaciones sobre las temperaturas.
- La comparación de tiempos de calentamiento o enfriamiento bajo condiciones iniciales y criterios definidos.
- La mejora obtenida y las suposiciones bajo las cuales es válida.
- Las conclusiones de la adaptación.

La reducción de una temperatura estacionaria no se utilizará, por sí sola, como demostración de un menor tiempo de enfriamiento.

## 5. Uso de inteligencia artificial y auditoría

Claude se utilizó como herramienta de apoyo para generar reportes, código, gráficas y documentos en distintos formatos.

Los prompts y las respuestas se conservan para documentar las solicitudes realizadas y los cambios entre versiones.

Las auditorías revisan:

- Los cálculos y sus unidades.
- La coherencia entre ecuaciones, tablas, gráficas y conclusiones.
- Las explicaciones incompletas o que requieren aclaración.
- La terminología y su relación con el material discutido en clase.
- Las afirmaciones y limitaciones de las comprobaciones realizadas.

La solución manual de las estudiantes se utiliza para contrastar los resultados generados con AI. Las comprobaciones computacionales se distinguen de la verificación manual.

Para el ejercicio original, la aprobación se documenta mediante la copia firmada de la versión 3. La documentación equivalente del ejercicio modificado se incorporará al completar esa etapa.
