# Proyecto de Transferencia de Calor — Ejercicio 5-34

**Estudiantes:**

- Karina Hernández Cruz
- Claudia Román García

Este proyecto presenta la solución del ejercicio original 5-34 y su adaptación para estudiar el comportamiento transitorio y lograr un enfriamiento más rápido.

El repositorio reúne cálculos manuales, conversaciones con Claude, reportes, código de Python, gráficas y auditorías. Las versiones se conservan para mostrar cómo evolucionó el trabajo, qué observaciones se identificaron y cómo se incorporaron las correcciones.

## 1. Organización y estado del proyecto

| Parte | Contenido | Estado |
| --- | --- | --- |
| Ejercicio original | Solución manual, tres versiones del reporte, conversaciones, código, gráficas, auditorías y reporte firmado | Finalizado; versión 3 aprobada por las estudiantes |
| Ejercicio modificado | Análisis transitorio, cambios de material, espesor y convección, y comparación de enfriamiento | Primera versión generada; en proceso de auditoría e incorporación al repositorio |
| Comparación final | Evaluación de la mejora y sus condiciones de validez | Pendiente de completar con los resultados finales revisados |

### Acceso a los documentos principales

- [Reporte final del ejercicio original, aprobado y firmado](01_Ejercicio_original/Version_3/Reporte_original_v3_aprobado_y_firmado.pdf)
- [Reporte final de Claude en PDF](01_Ejercicio_original/Version_3/Reporte_original_v3.pdf)
- [Auditoría de la versión 3](01_Ejercicio_original/Version_3/Auditoria_del_reporte_3.pdf)
- [Cálculos manuales del ejercicio original](01_Ejercicio_original/Calculo_manual_Ejercicio_original_5_34.pdf)
- [Conversación completa con Claude: versiones 1, 2 y 3](01_Ejercicio_original/Conversacion_completa_con_Claude.md)
- [Carpeta del ejercicio original](01_Ejercicio_original/)

**La versión 3 es el reporte final del ejercicio original. La copia aprobada y firmada documenta el cierre de esta parte del proyecto.**

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

El reporte se elaboró mediante un proceso de generación, auditoría y corrección. Las tres versiones documentan ese proceso; no representan tres ejercicios diferentes.

#### Versión 1 — Reporte inicial y primera auditoría

El primer prompt produjo el reporte inicial, el código de Python y la gráfica de temperaturas.

La primera revisión identificó explicaciones que requerían mayor claridad sobre las suposiciones, los balances de energía, la interfaz entre materiales, las unidades y la notación. Estas observaciones quedaron registradas en la auditoría y sirvieron para preparar el segundo prompt.

Esta versión se conserva como evidencia de la primera entrega generada con Claude.

#### Versión 2 — Incorporación de correcciones y segunda auditoría

La segunda versión incorporó las aclaraciones solicitadas a partir de la primera revisión.

La nueva auditoría identificó ajustes adicionales: corregir la descripción de la disminución de temperatura en el metal, precisar la explicación de los errores de punto flotante y actualizar el estado de la comparación manual.

Estas observaciones dieron origen al tercer prompt. Los ajustes no requirieron cambiar las temperaturas nodales ni el coeficiente de convección umbral.

#### Versión 3 — Confirmación manual y reporte final

La tercera versión incorporó las correcciones anteriores. Posteriormente, se actualizó dentro de esta misma versión el estado de las comprobaciones manuales confirmadas por las estudiantes.

**En las versiones 1 y 2 todavía no se había confirmado la verificación manual completa. Para la versión 3, Karina Hernández Cruz y Claudia Román García confirmamos la coincidencia de los cálculos revisados con nuestros cálculos manuales, considerando el redondeo.**

Esta confirmación se distingue de las comprobaciones computacionales realizadas por Claude. La verificación manual corresponde al trabajo de las estudiantes; no implica que Claude haya inspeccionado nuestro documento manual.

La revisión final quedó documentada en la auditoría de la versión 3 y la aprobación se registró mediante la copia firmada por ambas estudiantes.

Por ello, **la versión 3 se identifica como el reporte final del ejercicio original**. Las versiones 1 y 2 permanecen disponibles como evidencia del proceso de revisión.

La confirmación de los cálculos no modifica por sí sola el estado de revisión de las referencias a diapositivas, registrado por separado en la documentación.

### 2.3. Conversaciones con Claude

La conversación global reúne los prompts, las respuestas y los archivos entregados durante las tres versiones. También se conservan las conversaciones individuales dentro de cada carpeta.

| Registro | Acceso |
| --- | --- |
| Conversación global | [Leer las conversaciones completas](01_Ejercicio_original/Conversacion_completa_con_Claude.md) |
| Conversación de la versión 1 | [Leer prompt 1 y respuestas](01_Ejercicio_original/Version_1/Conversaci%C3%B3n_con_Claude.md) |
| Conversación de la versión 2 | [Leer prompt 2 y respuestas](01_Ejercicio_original/Version_2/Conversacion_con_Claude.md) |
| Conversación de la versión 3 | [Leer prompt 3, actualización y respuestas](01_Ejercicio_original/Version_3/Conversacion_con_Claude.md) |

Las auditorías se presentan como documentos separados. Las observaciones que se enviaron a Claude para solicitar correcciones aparecen en los prompts correspondientes.

### 2.4. Archivos de la versión 1

Primera entrega del ejercicio original y su auditoría.

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

Segunda entrega del ejercicio original y auditoría que dio lugar a los ajustes de la versión 3.

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

### 2.6. Archivos de la versión 3 — Reporte final

Los reportes en PDF, Word y Markdown corresponden a la entrega actualizada de la versión 3. El código y la gráfica se conservaron de la primera entrega de esta versión, según lo documentado en la conversación.

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

Los tres documentos PDF cumplen funciones distintas:

- **Reporte final:** presenta el desarrollo técnico generado con Claude y actualizado tras las correcciones.
- **Auditoría:** conserva las anotaciones y el cierre de la revisión.
- **Reporte aprobado y firmado:** documenta la aprobación de ambas estudiantes y constituye la copia final para la entrega.

[Explorar la carpeta de la versión 3](01_Ejercicio_original/Version_3/)

### 2.7. Comparación entre los cálculos manuales y el reporte final

Las estudiantes resolvieron el ejercicio manualmente y contrastaron sus resultados con los del reporte final generado con Claude. La siguiente tabla resume las temperaturas nodales y el coeficiente de convección umbral.

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

### 2.8. Interpretación de los resultados

#### Distribución de temperatura

La temperatura disminuye desde la base del metal hasta la superficie expuesta al aire, de acuerdo con la dirección de transferencia del calor.

La temperatura máxima se encuentra en el nodo 0 y es de **105.125 °C**. En la interfaz entre materiales es de aproximadamente **105 °C**, y en la superficie exterior es de **45 °C**.

#### Diferencia entre los materiales

La caída de temperatura en el metal es de **0.125 °C**, mientras que en la placa no metálica es de **60 °C**.

La mayor caída ocurre en la placa no metálica porque su resistencia térmica a la conducción es mucho mayor. Por eso, el perfil del metal parece casi horizontal en la gráfica general; la ampliación permite observar su pequeña disminución de temperatura.

#### Evaluación del límite de 93 °C

El ejercicio requiere evaluar el límite térmico; no presupone que las condiciones originales deban cumplirlo.

Con **h = 5 W/(m²·K)**, la temperatura máxima de **105.125 °C** supera el límite en **12.125 °C**. Por tanto, las condiciones originales no satisfacen el criterio térmico indicado.

#### Significado del coeficiente de convección umbral

El valor **h* = 1200/143 ≈ 8.391608 W/(m²·K)** produce una temperatura máxima de exactamente **93 °C**, manteniendo constantes los demás datos.

- **h = h*:** la temperatura máxima es igual a 93 °C.
- **h > h*:** la temperatura máxima es menor que 93 °C.

El valor 8.39 es una aproximación del umbral. Para establecer la condición estricta se conserva el valor exacto, ya que utilizar literalmente 8.39 produce una temperatura ligeramente superior a 93 °C.

#### Conclusión del ejercicio original

La solución manual y el reporte final de Claude coinciden en las temperaturas nodales y el coeficiente de convección umbral.

El análisis demuestra que las condiciones originales producen una temperatura máxima superior al límite indicado. Aumentar la convección por encima del umbral calculado permite reducir esa temperatura por debajo de 93 °C, manteniendo los demás datos constantes.

Las tres versiones documentan la revisión progresiva del reporte. La versión 3 incorpora las correcciones y la confirmación de la verificación manual, y cuenta con la aprobación firmada de ambas estudiantes.

## 3. Ejercicio modificado

**Estado: primera versión generada y en proceso de auditoría. La documentación se incorporará al repositorio conforme se organice y revise.**

Esta etapa amplía el ejercicio original mediante un análisis transitorio y una adaptación orientada a reducir el tiempo de enfriamiento.

### 3.1. Configuraciones propuestas

| Parámetro | Caso A — Configuración original | Caso B — Configuración modificada |
| --- | --- | --- |
| Placa inferior | SB-96, 30 mm | SB-96, 30 mm |
| Capa superior | Material no metálico | Aluminio |
| Espesor de la capa superior | 20 mm | 5 mm |
| Conductividad de la capa superior | 0.050 W/(m·K) | 237 W/(m·K) |
| Coeficiente de convección | 5 W/(m²·K) | 25 W/(m²·K) |
| Temperatura del aire | 15 °C | 15 °C |

La propuesta combina tres cambios: material de la capa superior, espesor y convección. La mejora se evalúa como resultado de esa combinación.

Las propiedades adicionales necesarias para calcular tiempos, sus fuentes y los supuestos del modelo se documentan en el reporte del ejercicio modificado.

### 3.2. Pruebas de calentamiento y enfriamiento

#### Calentamiento

Ambos sistemas comienzan uniformemente a 15 °C y reciben un flujo de calor de 150 W/m² por la superficie inferior.

Se estudian la evolución de las temperaturas, el tiempo para completar el 95 % del aumento de temperatura y el cumplimiento del límite térmico de 93 °C.

#### Enfriamiento

Se realiza una prueba independiente con ambos sistemas inicialmente a 90 °C, el calentamiento apagado y aire a 15 °C.

La superficie inferior se considera adiabática. Se compara el tiempo necesario para que la temperatura máxima de cada sistema disminuya hasta 60 °C. Cada configuración conserva sus materiales, espesores y coeficiente de convección.

Esta comparación permite evaluar directamente el enfriamiento bajo temperaturas inicial y objetivo comunes.

### 3.3. Proceso de trabajo y documentación

El ejercicio modificado tiene su propia numeración de versiones, comenzando por la versión 1.

La primera entrega se revisa para comprobar los cálculos y detectar explicaciones que requieren corrección o mayor claridad. Las observaciones de la auditoría servirán para preparar la siguiente versión.

Se conservarán:

- Los prompts y las respuestas de Claude.
- La conversación global y las conversaciones individuales.
- Los reportes en PDF, Word y Markdown.
- El código de Python.
- Las gráficas y tablas de resultados.
- Los cálculos manuales.
- Las auditorías y las correcciones.
- El reporte final aprobado y firmado.

Los enlaces se incorporarán cuando los archivos estén disponibles en el repositorio.

### 3.4. Verificación e interpretación

Se distinguen las aproximaciones analíticas de los resultados numéricos. También se documentan las comprobaciones de estabilidad, convergencia y balance de energía.

La comparación manual se presentará en una tabla independiente de la del ejercicio original. No se identificará una versión como aprobada hasta completar su revisión y documentar la confirmación de las estudiantes.

Los resultados finales de esta etapa se incorporarán después de revisar el reporte y completar la verificación correspondiente.

## 4. Comparación final del proyecto

**Estado: pendiente de completar con los resultados finales revisados del ejercicio modificado.**

La comparación explicará:

- Qué parámetros se conservaron y cuáles se modificaron.
- Cómo cambiaron las resistencias y el almacenamiento térmico.
- Cómo se modificaron las temperaturas estacionarias.
- Cuánto se redujo el tiempo de enfriamiento entre las temperaturas comunes seleccionadas.
- Bajo qué supuestos y condiciones es válida la mejora.

El ejercicio original aporta la solución estacionaria de referencia. Su extensión transitoria, denominada caso A, permite comparar tiempos con el caso B modificado.

Una temperatura estacionaria menor no se utilizará, por sí sola, como prueba de un enfriamiento más rápido.

## 5. Uso de inteligencia artificial y auditoría

Claude se utiliza como herramienta de apoyo para generar reportes, código, gráficas y documentos. ChatGPT también se utiliza como apoyo para organizar el proyecto, preparar prompts y revisar el planteamiento y los resultados.

Las comprobaciones realizadas mediante herramientas computacionales se distinguen de la verificación manual de las estudiantes.

Las auditorías evalúan:

- Los cálculos y sus unidades.
- La coherencia entre ecuaciones, tablas, gráficas y conclusiones.
- Los supuestos y los límites de los métodos empleados.
- Las explicaciones incompletas o que necesitan aclaración.
- La terminología y su relación con el material discutido en clase.
- Las afirmaciones que requieren evidencia o corrección.

Las conversaciones registran las solicitudes y respuestas. Las auditorías documentan las observaciones de revisión. Los cálculos manuales permiten contrastar los resultados, y el reporte firmado registra la aprobación final de las estudiantes.

Para el ejercicio original, este proceso culminó en la **versión 3 aprobada y firmada**. La documentación equivalente del ejercicio modificado se incorporará al completar su desarrollo y revisión.
