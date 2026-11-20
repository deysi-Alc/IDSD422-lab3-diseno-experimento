# Plantilla de protocolo — Experimento de ubicación de producto

**Equipo:** 3 · **Integrantes:** Jhon Solorzano, Said Bravo, David Jácome, Deysi Guachamin · **Fecha:** 19/11/2026

**Repositorio (fork):** https://github.com/deysi-Alc/IDSD422-lab3-diseno-experimento

Completa cada sección. Usa commits por sección; la historia del repositorio se revisa.

## 1. Pregunta e hipótesis

**Pregunta:** ¿El producto estrella vende más en promedio cuando se ubica en el pasillo principal que en su ubicación habitual, medido en ventas semanales durante 4 semanas?

- **H0:** la venta semanal promedio del producto es igual en el pasillo principal y en la ubicación habitual.
- **H1:** la venta semanal promedio (USD) del producto es mayor en el pasillo principal que en la ubicación habitual.

La hipótesis es medible: se compara el promedio de `ventas_producto` por semana entre las tienda-semana con cada ubicación.

## 2. Unidad experimental

*¿Quién recibe el tratamiento? ¿Cuántas unidades se incluyen?*

- **Unidad:** **tienda-semana** (una tienda observada durante una semana con una ubicación determinada del producto).
- **Número de unidades y justificación:** 10 tiendas × 4 semanas = **40 unidades**. Se experimenta en 10 tiendas de distintas ciudades y cada una se observa 4 semanas; así cada tienda recibe las dos ubicaciones y sirve como su propia referencia, y el período es corto para no detener el negocio.

## 3. Factor, niveles y tratamiento

- **Factor** (variable manipulada): ubicación del producto estrella.
- **Niveles** (valores del factor): `pasillo_principal` y `habitual` (ubicación actual).
- **Tratamiento** (combinación asignada): el producto en el pasillo principal durante una semana; en la semana siguiente vuelve a su ubicación habitual (control). Las ubicaciones se alternan semana a semana durante las 4 semanas.

## 4. Grupo de control

*¿Cuál es la referencia sin tratamiento y qué rol cumple?*

Es la misma tienda con el producto en su ubicación habitual (20 tienda-semana de las 40). Su rol es dar la referencia contra la que se compara el pasillo principal: si las ventas suben solo cuando el producto está en el pasillo principal, y no en las semanas de control, la diferencia se puede atribuir a la ubicación y no a otra cosa.

## 5. Aleatorización

*¿Cómo se asignan las unidades a los grupos? ¿Por qué es necesaria?*

Todas las tiendas participan **al mismo tiempo** (en paralelo). Lo que se sortea es con qué ubicación empieza cada tienda: 5 de las 10 tiendas empiezan en pasillo principal y 5 en la ubicación habitual, y después alternan cada semana. Así, en cada semana hay 5 tiendas con tratamiento y 5 con control, y cada grupo termina con 20 tienda-semana.

El sorteo es necesario porque reparte al azar entre los dos grupos los factores que no controlamos ni conocemos (tamaño de la tienda, tipo de cliente, ciudad) y el orden en que se aplica cada ubicación (que el tratamiento no caiga siempre en la semana 1 o 2). Como el investigador es quien asigna con código, es un experimento y no un estudio observacional.

- **Línea de código de la asignación (Python):**

```python
import numpy as np

tiendas = ["Quito Norte", "Quito Sur", "Guayaquil Centro", "Guayaquil Norte",
           "Cuenca Centro", "Cuenca Sur", "Ambato Centro", "Manta", "Loja", "Machala"]
rng = np.random.default_rng(2026)   # semilla fija: la corrida se puede repetir

# Línea de asignación: 5 tiendas empiezan en pasillo_principal y 5 en habitual, al azar
inicio = rng.permutation(["pasillo_principal"] * 5 + ["habitual"] * 5)
```

- **Resultado de una corrida (semilla 2026):**

| Tienda | Empieza en (semana 1) | Semana 2 | Semana 3 | Semana 4 |
|---|---|---|---|---|
| Quito Norte | pasillo_principal | habitual | pasillo_principal | habitual |
| Quito Sur | habitual | pasillo_principal | habitual | pasillo_principal |
| Guayaquil Centro | pasillo_principal | habitual | pasillo_principal | habitual |
| Guayaquil Norte | habitual | pasillo_principal | habitual | pasillo_principal |
| Cuenca Centro | habitual | pasillo_principal | habitual | pasillo_principal |
| Cuenca Sur | pasillo_principal | habitual | pasillo_principal | habitual |
| Ambato Centro | habitual | pasillo_principal | habitual | pasillo_principal |
| Manta | pasillo_principal | habitual | pasillo_principal | habitual |
| Loja | habitual | pasillo_principal | habitual | pasillo_principal |
| Machala | pasillo_principal | habitual | pasillo_principal | habitual |

Resultado: 20 tienda-semana con `pasillo_principal` y 20 con `habitual`. Con la misma semilla la asignación sale siempre igual; con otra semilla cambian las tiendas, no el reparto 5/5. El código completo está en `scripts/comparacion_experimento.py`.

## 6. Respuesta y medición

- **Variable respuesta:** ventas semanales del producto, en USD (`ventas_producto`).
- **Período de medición:** 4 semanas, todas las tiendas a la vez.
- **Quién registra y cómo (¿ciego?):** el registro es automático desde el POS (punto de venta), por lo que no depende de la opinión del personal. El personal de tienda no puede ser ciego, porque ve dónde está el producto; el ciego se aplica al análisis: quien compara los datos recibe los grupos con códigos (A y B) y no sabe cuál es el tratamiento hasta terminar el cálculo.

## 7. Factores a controlar (mínimo 4)

| Factor a controlar | Cómo se controla o registra |
|---|---|
| 1. Clima | Registrar temperatura y lluvia de cada semana y ciudad. Como cada semana hay tiendas de los dos grupos, el clima afecta a ambos por igual. |
| 2. Evento local | Armar antes del inicio un calendario de feriados y eventos por ciudad y anotarlos en `notas`; si un evento cae en una tienda-semana, se marca para revisarla aparte. |
| 3. Surtido / stock | Verificar que el producto tenga stock todos los días; una tienda-semana con quiebre de stock se marca y se analiza por separado. |
| 4. Cambios en el personal | Mantener turnos y personal sin cambios durante las 4 semanas y registrar cualquier cambio. |
| 5. Promociones del producto y de la competencia | Sin promociones propias en el período; las ajenas se anotan en `promocion_simultanea`. |
| 6. Precio | Mantener el precio fijo durante el experimento. |

## 8. Limitaciones del diseño

*¿Qué podría invalidar el experimento si no se controla? ¿Qué no se podrá concluir?*

- **Pérdida de potencia por promociones:** si un producto competidor está en promoción esa semana, es más probable que se compre ese y no el producto que estamos probando, y eso esconde el efecto de la ubicación.
- **Canibalización:** el pasillo principal tiene un espacio limitado; al mover el producto estrella ahí se desplaza otro producto, y las ventas que gana uno pueden ser ventas que pierde el otro. Medir solo el producto estrella no lo detecta; convendría registrar también las ventas de la categoría.
- **Efecto arrastre entre semanas:** los clientes pueden acostumbrarse a la ubicación de la semana anterior, y eso mezcla el efecto de una semana con el de la siguiente.
- **Pocas unidades y poco tiempo:** 10 tiendas y 4 semanas no representan a toda la cadena ni a las temporadas altas, así que la conclusión vale para estas tiendas en ese período.
- **No se puede concluir** por qué la ubicación cambia las ventas, solo si las cambia. El experimento no se ejecutó en esta práctica; se evalúa la coherencia del diseño.

## 9. Comparación en código (Python/R)

*Escribe `scripts/comparacion_experimento.py` (o `.R`): debe cargar `plantillas/registro_experimento.csv` y calcular el promedio de `ventas_producto` por `ubicacion`. Incluye la salida y responde:*

**Salida (`python scripts/comparacion_experimento.py`):**

```
ubicacion
habitual             1040.0
pasillo_principal    1335.0
Name: ventas_producto, dtype: float64
*****
ubicacion
pasillo_principal    2
habitual             2
Name: count, dtype: int64
```

- **¿Qué grupo muestra mayor venta promedio en la plantilla?**
  El pasillo principal muestra 1335 USD en venta frente a 1040 USD de la ubicación habitual (295 USD más).

- **¿Por qué con 4 filas no se puede concluir nada sobre el efecto de la ubicación?**
  No se puede concluir porque no hubo asignación aleatoria, los datos son muy pocos (4 filas, 2 por grupo), cada tienda aparece una sola vez y en una sola ubicación (el efecto de la ubicación se mezcla con la ciudad y el tamaño de la tienda), una de las tiendas del pasillo principal tenía una promoción simultánea (Guayaquil Centro) y no hay una medida de variabilidad.

- **Si el experimento se ejecutara con tu protocolo, ¿qué le faltaría a este análisis para ser justo?**
  Usar las 40 tienda-semana con la asignación aleatoria de la sección 5; comparar cada tienda contra sí misma (diferencia de ventas entre sus semanas con pasillo principal y con ubicación habitual); medir la variabilidad (desviación estándar y una prueba o intervalo para la diferencia); y excluir o ajustar las tienda-semana con promoción, quiebre de stock o eventos locales.

## 10. Bonus: adaptación a un ensayo clínico (vacuna)

El mismo diseño, adaptado a probar una vacuna:

| Elemento | Experimento de ubicación | Ensayo clínico de vacuna |
|---|---|---|
| Unidad | tienda-semana | participante voluntario |
| Factor y niveles | ubicación: pasillo principal / habitual | tratamiento: vacuna / placebo |
| Grupo de control | producto en la ubicación habitual | placebo (inyección sin el principio activo) |
| Aleatorización | sorteo 5/5 de la ubicación inicial | sorteo 1:1 de cada participante a vacuna o placebo |
| Ciego | solo en el análisis | doble ciego: ni el participante ni quien evalúa saben quién recibió qué |
| Respuesta | ventas semanales (USD) | casos confirmados de la enfermedad en un período fijo |
| Factores a controlar | clima, eventos, stock, personal | edad, sexo, riesgo de exposición, enfermedades previas |

Diferencia clave: el diseño cruzado no sirve para una vacuna, porque no se puede "quitar" la vacuna después de aplicarla; por eso los grupos son paralelos y cada participante recibe un solo tratamiento. También se requiere consentimiento informado y aprobación de un comité de ética.
