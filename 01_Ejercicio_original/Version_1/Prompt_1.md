# Prompt 1 - Ejercicio original 5-34

Somos dos estudiantes de Ingeniería Química trabajando como ingenieras principiantes en un proyecto de Transferencia de Calor. Ayúdanos a preparar la primera versión del informe técnico del ejercicio original 5-34. Esta versión será comparada con nuestros cálculos manuales antes de preparar el informe final.

Explica en español, con un nivel apropiado para estudiantes del curso: claro, paso a paso y con ecuaciones, sustituciones y unidades.

1. MATERIAL DE REFERENCIA

Revisa los archivos adjuntos antes de resolver:

- 092126 2.pdf: instrucciones del proyecto, rúbrica y enunciado del ejercicio 5-34. Revisa también la figura que continúa en la página siguiente.
- Libreta.pdf: utiliza el procedimiento de balances de energía y diferencias finitas presentado en clase.
- Libreta Examen 2.pdf: consulta el contenido pertinente sobre conducción y resistencias térmicas.
- Plantilla de prompts del GitHub de la clase, si está adjunta: respeta su estructura.

Identifica las páginas o diapositivas que realmente consultes. Si falta un archivo, no puedes leerlo o no encuentras una referencia, indícalo claramente. No inventes citas ni afirmes haber utilizado material que no revisaste.

2. ALCANCE

Resuelve únicamente el ejercicio original 5-34 mediante diferencias finitas en estado estacionario. No desarrolles todavía el ejercicio adaptado.

El proyecto completo requiere posteriormente una modificación que demuestre calentamiento o enfriamiento más rápido. Al final puedes indicar brevemente qué información adicional necesitaremos para esa etapa, pero no inventes propiedades ni confundas una temperatura estacionaria menor con un menor tiempo de enfriamiento.

3. DATOS DEL EJERCICIO

Comprueba estos datos contra el enunciado y su figura antes de utilizarlos:

- Placa metálica: k_m = 36 W/(m·K), L_m = 0.030 m.
- Placa no metálica: k_n = 0.05 W/(m·K), L_n = 0.020 m.
- Flujo de calor entrante en la superficie inferior del metal: q″ = 150 W/m².
- Convección en la superficie superior del no metal: h = 5 W/(m²·K).
- Temperatura del aire: T∞ = 15 °C.
- Espaciamiento uniforme: Δx = 0.005 m.
- Límite de temperatura del metal: 93 °C.

Si encuentras alguna discrepancia, señálala antes de continuar.

Define x desde la superficie inferior del metal hacia la superficie superior del no metal. Utiliza 11 nodos, numerados del 0 al 10, con la interfaz en el nodo 6, x = 0.030 m.

4. DESARROLLO DEL INFORME

Organiza el informe con las siguientes partes:

A. Objetivo y descripción del sistema
Explica qué se busca, cómo entra y sale el calor y cuáles son las incógnitas. Incluye una tabla de datos con unidades.

B. Suposiciones
Distingue las condiciones dadas por el enunciado de las suposiciones adoptadas. Explica el estado estacionario, la conducción unidimensional, las conductividades constantes por material, la ausencia de generación interna, el contacto térmico perfecto y la radiación despreciable.

C. Distribución de los nodos
Identifica las fronteras, los nodos interiores y la interfaz mediante una tabla o esquema sencillo.

D. Formulación por diferencias finitas
Parte del balance general de energía y muestra qué términos se eliminan al aplicar las suposiciones.

Deriva las ecuaciones correspondientes a:
- La frontera con flujo impuesto.
- Un nodo interior del metal.
- Un nodo interior del no metal.
- La interfaz entre los materiales.
- La frontera con convección.

Explica los signos, las distancias entre nodos y la cancelación del área. Distingue el ancho del volumen de control de frontera de la distancia entre nodos vecinos. Conserva las conductividades correspondientes a cada lado de la interfaz.

E. Solución
Presenta las 11 ecuaciones con sus coeficientes numéricos y unidades. Desarrolla un procedimiento algebraico ordenado que podamos seguir a mano y resuelve también el sistema con Python.

F. Resultados e interpretación
Incluye:
- Tabla de temperatura para los nodos 0 a 10.
- Gráfica de T frente a x, con unidades, materiales, interfaz y límite de 93 °C.
- Una ampliación del perfil dentro del metal.
- Explicación de las pendientes usando la ley de Fourier.
- Caídas de temperatura en cada material y entre la superficie exterior y el aire.
- Ubicación y valor de la temperatura máxima del metal.
- Evaluación del cumplimiento del límite del ejercicio.

G. Coeficiente de convección requerido
Calcula el valor umbral de h que produce una temperatura máxima de 93 °C, manteniendo constantes los demás datos.

Muestra el despeje y comprueba el resultado. Distingue entre alcanzar exactamente 93 °C y mantenerse estrictamente por debajo. Evalúa también h = 8.5 W/(m²·K).

H. Comprobaciones
Contrasta la solución de diferencias finitas con una solución independiente mediante resistencias térmicas.

Comprueba:
- Las temperaturas nodales.
- El balance global de energía.
- El flujo en cada tramo.
- La continuidad del flujo en la interfaz.
- Las condiciones de frontera.
- Los residuos de las 11 ecuaciones.

Define qué es un residuo y calcúlalo utilizando balances expresados en W/m² y temperaturas numéricas sin redondear. Distingue R, en K/W, de R″, en m²·K/W.

Conserva la precisión interna y redondea únicamente los resultados presentados. No interpretes un residuo pequeño como prueba suficiente de que el planteamiento físico es correcto.

5. ARCHIVOS QUE DEBES ENTREGAR

- reporte_original_v1.md: informe completo.
- ej_5_34_v1.py: código completo y reproducible.
- T_vs_x_5_34_v1.png: gráfica generada por ese código.

El código debe resolver el sistema, mostrar las temperaturas, calcular los flujos y residuos, comparar con resistencias térmicas, evaluar h y generar la gráfica. Incluye instrucciones breves para ejecutarlo y las bibliotecas necesarias.

Si puedes ejecutar el código, presenta los resultados reales de la ejecución. Si no puedes ejecutarlo o adjuntar archivos, dilo claramente y proporciona el contenido completo para guardarlo. No afirmes que ejecutaste, generaste o verificaste archivos si no lo hiciste.

6. REVISIÓN Y PRESENTACIÓN

Redacta el informe con estilo técnico claro y sin comentarios conversacionales innecesarios. Explica cualquier concepto adicional indispensable y evita incluir métodos que no corresponden a este ejercicio.

Al final, añade una lista breve de los cálculos que debemos contrastar con nuestra solución manual y de cualquier comprobación pendiente.

Antes de entregar, comprueba la consistencia entre el enunciado, las ecuaciones, la tabla, la gráfica, el código y las conclusiones.
