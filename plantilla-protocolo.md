# Plantilla de diseño — Encuesta de satisfacción (Hito 1)

**Asignatura:** Estadística y Programación para Ciencia de Datos I (IDSD422)  
**Institución:** Escuela Politécnica Nacional  
**Empresa:** RetailAndina S.A.  
**Equipo:** 3  
**Integrantes:**
- Jhon Solorzano
- Said Bravo
- David Jácome
- Deysi Guachamin

**Fecha:** 26/10/2026  
**Repositorio (fork):** https://github.com/Daxin7/IDSD422-lab2-diseno-encuesta  
**Enfoque del equipo (propuesto, pendiente de aprobación):** Satisfacción general y beneficios esperados de un programa de fidelización en compradores adultos de Quito.

---

## 1. Objetivo de la encuesta

**Objetivo general:**

Medir el nivel de satisfacción general de al menos 20 consumidores adultos que realizan compras en supermercados de Quito, así como su disposición a recomendar el establecimiento, su interés en participar en un programa de fidelización y los beneficios que consideran más atractivos, mediante una encuesta estructurada, con la finalidad de apoyar a la gerencia de RetailAndina S.A. en el diseño inicial de su programa de fidelización.

**Objetivos específicos:**

1. Determinar la distribución de los niveles de satisfacción de los consumidores mediante una escala ordinal de 1 a 5.
2. Identificar la proporción de encuestados que recomendarían su supermercado habitual.
3. Determinar el interés de los consumidores en participar en un programa de fidelización.
4. Identificar el beneficio más valorado por los participantes, entre descuentos, acumulación de puntos, promociones personalizadas, recompensas y otros beneficios.
5. Explorar la relación descriptiva entre la frecuencia de compra, la satisfacción general y la disposición a recomendar el establecimiento.

**Decisión gerencial que apoyará la encuesta:**

La gerencia podrá utilizar los resultados para priorizar los beneficios que debería ofrecer un programa de fidelización y detectar oportunidades de mejora en la experiencia general del consumidor.

**Indicadores propuestos:**

- **Satisfacción promedio:** suma de puntuaciones de satisfacción dividida entre el número de respuestas válidas, utilizada como resumen descriptivo de una escala ordinal.
- **Porcentaje de satisfacción favorable:** proporción de participantes que seleccionen 4 o 5 en la escala de satisfacción.
- **Porcentaje de recomendación:** proporción de participantes que respondan "Si" a la pregunta sobre recomendación.
- **Porcentaje de interés:** proporción de participantes que manifiesten interés en un programa de fidelización.
- **Beneficio preferido:** categoría con mayor frecuencia absoluta y relativa entre los beneficios propuestos.

Estos indicadores serán descriptivos y exploratorios. Debido al método de muestreo y al tamaño reducido de la muestra, sus resultados no se interpretarán como estimaciones representativas de todos los consumidores de Quito.

## 2. Población objetivo

**Población:**

Personas de 18 años o más, residentes en el Distrito Metropolitano de Quito, que hayan realizado compras de productos de consumo masivo en supermercados al menos una vez durante los últimos 30 días.

Para mantener la coherencia del cuestionario, se solicitará a cada participante que responda considerando el supermercado en el que compra con mayor frecuencia.

**Límites y justificación:**

| Criterio | Delimitación | Justificación |
|---|---|---|
| Región geográfica | Distrito Metropolitano de Quito | Permite realizar una recolección alcanzable para los integrantes del equipo. |
| Edad | Personas de 18 años o más | Facilita la participación autónoma y evita procedimientos adicionales relacionados con menores de edad. |
| Frecuencia de compra | Al menos una compra durante los últimos 30 días | Permite recopilar experiencias recientes de compra. |
| Tipo de establecimiento | Supermercados de productos de consumo masivo | Mantiene la investigación relacionada con el sector comercial de RetailAndina. |
| Residencia | Residentes de Quito | Evita mezclar experiencias de ciudades con condiciones comerciales diferentes. |
| Participación | Voluntaria, con consentimiento informado | Respeta la autonomía y privacidad de los participantes. |

**Criterios de inclusión:**

- Tener al menos 18 años.
- Residir en Quito.
- Haber comprado en un supermercado durante los últimos 30 días.
- Aceptar voluntariamente participar en la encuesta.
- Responder una sola vez al cuestionario.

**Criterios de exclusión:**

- Personas menores de 18 años.
- Personas que no residen en Quito.
- Personas que no hayan comprado en supermercados durante los últimos 30 días.
- Registros duplicados, respuestas sin consentimiento o formularios que no permitan comprobar los criterios de elegibilidad.

**Unidad de análisis:**

Cada consumidor adulto elegible que complete la encuesta.

**Marco de selección:**

Contactos y personas referidas a las que los integrantes del equipo puedan acceder y que cumplan los criterios establecidos.

No se dispone de un listado completo de todos los compradores adultos de supermercados de Quito. Por tanto, la población objetivo es más amplia que el conjunto de personas accesibles, una limitación que deberá considerarse en la interpretación de resultados.

## 3. Método de muestreo

**Método:**

Muestreo no probabilístico por conveniencia, complementado con referencias de participantes y una selección aleatoria reproducible únicamente cuando exista un listado de candidatos elegibles.

**Justificación:**

Se selecciona este método debido a que el equipo no dispone de un marco muestral completo de consumidores de supermercados de Quito, ni del presupuesto y tiempo necesarios para implementar un muestreo probabilístico de toda la población.

La selección por conveniencia permite contactar participantes elegibles mediante redes personales, familiares, compañeros y otros contactos disponibles, utilizando formularios digitales o encuestas presenciales.

Sin embargo, se reconoce que este procedimiento no garantiza que todos los integrantes de la población tengan una probabilidad conocida y distinta de cero de ser seleccionados. Por lo tanto, no corresponde generalizar estadísticamente los resultados al conjunto de consumidores de Quito.

**Tamaño y justificación:**

Se establece una meta de **24 respuestas reales**, distribuidas equitativamente entre los cuatro integrantes del equipo:

| Integrante | Respuestas reales previstas |
|---|---:|
| Jhon Solorzano | 6 |
| Said Bravo | 6 |
| David Jácome | 6 |
| Deysi Guachamin | 6 |
| **Total** | **24** |

Este tamaño se encuentra dentro del intervalo de 15 a 30 respuestas reales establecido para el laboratorio.

La muestra permite obtener un análisis descriptivo inicial, evaluar el funcionamiento del cuestionario y practicar procedimientos de limpieza y verificación de datos. No se considera suficiente para garantizar representatividad estadística.

En caso de incorporar respuestas simuladas para prácticas posteriores de programación, estas se identificarán explícitamente con `origen = simulada`, sin mezclarlas con las observaciones reales durante el análisis de resultados.

**Cómo se seleccionarán los participantes:**

1. Cada integrante elaborará una lista de posibles participantes adultos residentes en Quito.
2. Se comprobará que hayan comprado en un supermercado durante los últimos 30 días.
3. Se invitará a participar a personas con diferentes edades y frecuencias de compra, evitando depender exclusivamente de un mismo grupo de compañeros.
4. Se explicará el propósito académico de la investigación, el carácter voluntario de la participación y la política de confidencialidad.
5. Se aplicará una sola encuesta por participante.
6. Se registrará la cantidad de invitaciones realizadas, formularios completados y personas que no respondieron o rechazaron participar.
7. Se incorporarán únicamente los registros válidos al conjunto de datos de análisis.

**Equivalente en código (Python):**

El siguiente procedimiento permite seleccionar de manera reproducible hasta 24 candidatos de un archivo `clientes.csv`, suponiendo que este contiene las columnas `ciudad`, `edad` y `compra_ultimos_30_dias`.

```python
import pandas as pd

clientes = pd.read_csv("clientes.csv")

elegibles = clientes.loc[
    clientes["ciudad"].eq("Quito")
    & clientes["edad"].ge(18)
    & clientes["compra_ultimos_30_dias"].eq("Si")
]

muestra = elegibles.sample(
    n=min(24, len(elegibles)),
    random_state=42
)

print(muestra)
print("Candidatos seleccionados:", len(muestra))
```

**Justificación del código:**

La función `sample()` realiza una selección pseudoaleatoria dentro del listado disponible. El parámetro `random_state=42` permite reproducir el resultado cuando los datos de entrada permanecen iguales.

Sin embargo, esta aleatorización no transforma el diseño completo en un muestreo aleatorio simple de toda la población. Como el archivo inicial puede contener únicamente contactos accesibles, el procedimiento sigue limitado por el sesgo de cobertura del marco de selección.

La selección aleatoria simple sería preferible para realizar inferencias sobre toda la población si existiera un marco muestral completo y actualizado. En este laboratorio se declara de forma transparente la conveniencia como método principal, puesto que es viable y coherente con los recursos disponibles.

**Resultado de la ejecución:**

Pendiente de generar a partir de una lista real de candidatos elegibles. No se reportan participantes seleccionados ni respuestas recolectadas antes de realizar el procedimiento.

## 4. Cuestionario (5–10 preguntas)

**Instrucciones para el encuestado:**

Esta encuesta forma parte de una actividad académica de la Escuela Politécnica Nacional y busca conocer la satisfacción y las expectativas de consumidores de supermercados de Quito. La participación es voluntaria, anónima y con fines exclusivamente académicos.

Para las preguntas relacionadas con la experiencia de compra, considere el supermercado en el que compra con mayor frecuencia.

**Preguntas de elegibilidad previas:**

- ¿Tiene 18 años o más? Si / No.
- ¿Reside en Quito? Si / No.
- ¿Ha realizado al menos una compra en un supermercado durante los últimos 30 días? Si / No.

Estas preguntas se utilizan como filtro de inclusión y no forman parte de las ocho preguntas principales.

### Cuestionario principal

| # | Pregunta | Tipo de variable | Dtype al cargar | Opciones / escala |
|---|---|---|---|---|
| 1 | ¿Cuál es su edad en años cumplidos? | Numérica discreta | `int64` | Entero igual o mayor que 18 |
| 2 | ¿Con qué frecuencia realiza compras en el supermercado que visita habitualmente? | Categórica ordinal | `object` | Varias veces por semana; Semanal; Quincenal; Mensual; Menos de una vez al mes |
| 3 | En general, ¿qué tan satisfecho está con el supermercado donde compra habitualmente? | Categórica ordinal | `int64` | 1 = Muy insatisfecho; 2 = Insatisfecho; 3 = Ni satisfecho ni insatisfecho; 4 = Satisfecho; 5 = Muy satisfecho |
| 4 | ¿Recomendaría a otra persona el supermercado donde compra habitualmente? | Categórica binaria | `object` | Si; No |
| 5 | ¿Qué tanto le interesaría participar en un programa de fidelización de un supermercado? | Categórica ordinal | `int64` | 1 = Nada interesado; 2 = Poco interesado; 3 = Ni interesado ni desinteresado; 4 = Interesado; 5 = Muy interesado |
| 6 | ¿Cuál de los siguientes beneficios preferiría recibir mediante un programa de fidelización? | Categórica nominal | `object` | Descuentos directos; Acumulación de puntos; Promociones personalizadas; Productos o recompensas gratuitas; Otro; Ninguno |
| 7 | ¿Cuál es el principal aspecto que considera que debería mejorar el supermercado donde compra habitualmente? | Categórica nominal | `object` | Precios; Atención al cliente; Rapidez en caja; Variedad de productos; Disponibilidad de productos; Limpieza y comodidad; Ninguno; Otro |
| 8 | ¿Desea agregar algún comentario o sugerencia sobre su experiencia de compra? | Categórica nominal (texto libre) | `object` | Respuesta abierta y opcional |

**Nota sobre los tipos de variables:**

La clasificación conceptual no depende únicamente del tipo de dato que detecta pandas. Por ejemplo, `satisfaccion_general` se almacena como un entero, pero representa una variable categórica ordinal, porque sus valores expresan categorías ordenadas y no magnitudes físicas continuas.

En el caso de `edad`, se registra en años cumplidos, por lo que se trata operativamente como numérica discreta.

El comentario abierto es información cualitativa no estructurada. Aunque puede almacenarse como `object`, no debe interpretarse automáticamente como una variable cuantitativa ni como una escala ordinal.

### Nombres de las columnas

Para almacenar las respuestas en el CSV se propone el siguiente esquema:

| Columna | Descripción |
|---|---|
| `respuesta_id` | Identificador anónimo, por ejemplo R001 |
| `fecha` | Fecha de aplicación en formato ISO `YYYY-MM-DD` |
| `ciudad` | Quito, ciudad de residencia verificada mediante pregunta filtro |
| `edad` | Edad del participante |
| `frecuencia_visita` | Frecuencia de compra |
| `satisfaccion_general` | Nivel de satisfacción (1–5) |
| `recomendaria` | Si / No |
| `interes_programa` | Nivel de interés (1–5) |
| `beneficio_preferido` | Beneficio seleccionado |
| `aspecto_mejora` | Aspecto prioritario de mejora |
| `comentario` | Comentario opcional |
| `origen` | real / simulada |

Las columnas `respuesta_id`, `fecha`, `ciudad` y `origen` son metadatos del registro o filtros de elegibilidad, no preguntas adicionales del cuestionario principal.

### Reglas para registrar las respuestas

- Utilizar exactamente las categorías especificadas.
- No utilizar distintas grafías para la misma opción, como `Sí`, `si` y `SI`.
- Guardar un registro por participante.
- No registrar nombres, cédulas, direcciones o números telefónicos.
- Mantener vacía la celda `comentario` cuando el participante no desee responder.
- Diferenciar estrictamente las observaciones reales de las simuladas.
- Validar que `edad >= 18` y que las puntuaciones ordinales estén comprendidas entre 1 y 5.

## 5. Análisis de sesgos

| Sesgo potencial | Mitigación |
|---|---|
| **1. Sesgo de selección o cobertura:** al contactar principalmente familiares, amigos y compañeros, podrían participar personas con edades, hábitos y condiciones socioeconómicas semejantes. | Diversificar los contactos, reclutar personas de distintos grupos de edad y frecuencias de compra, distribuir las invitaciones entre los cuatro integrantes y reconocer explícitamente el carácter no probabilístico de la muestra. |
| **2. Sesgo de no respuesta y de respuesta:** algunas personas podrían ignorar la encuesta o responder favorablemente por cortesía, especialmente si conocen al encuestador. | Registrar invitaciones y rechazos, mantener un cuestionario breve y neutral, explicar que no existen respuestas correctas, permitir respuestas anónimas y evitar que el encuestador influya en las opciones elegidas. |

**Análisis complementario:**

El sesgo de selección podría observarse si una gran mayoría de participantes perteneciera a un mismo intervalo de edad o tuviera la misma frecuencia de compra. Esto no demuestra por sí solo la existencia de sesgo, pero advierte una posible falta de diversidad.

El sesgo de no respuesta podría sospecharse si muchos participantes invitados no completan el formulario, especialmente cuando la falta de respuesta se concentra en un grupo conocido de invitados.

El sesgo de respuesta podría manifestarse mediante una concentración poco habitual de puntuaciones máximas de satisfacción o recomendación. Sin embargo, un porcentaje elevado de respuestas positivas no constituye una demostración de sesgo: también puede reflejar satisfacción auténtica.

**Indicador adicional de no respuesta:**

Se calculará la tasa de respuesta:

\[
\text{Tasa de respuesta} =
\frac{\text{Encuestas completas válidas}}
{\text{Personas elegibles invitadas}} \times 100
\]

Se registrarán las invitaciones, las respuestas completas y los rechazos, sin publicar información personal de quienes no participaron.

**Limitación metodológica:**

Debido a la selección no probabilística, las conclusiones tendrán alcance exploratorio. No se utilizarán intervalos de confianza ni márgenes de error propios de un muestreo probabilístico para afirmar representatividad poblacional.

## 6. Confidencialidad (RA3)

**Datos personales que se piden y por qué:**

La encuesta solicitará únicamente datos mínimos necesarios para alcanzar sus objetivos.

- **Edad:** permitirá identificar el perfil etario de los participantes y comprobar el criterio de inclusión.
- **Ciudad de residencia:** permitirá verificar que el participante pertenece a la población definida.
- **Respuestas de consumo:** permitirán analizar frecuencia de compra, satisfacción, recomendación e interés en programas de fidelización.

No se solicitarán nombres, cédulas de identidad, números telefónicos, correos electrónicos, direcciones domiciliarias ni información financiera.

**Plan de anonimización:**

1. Asignar un identificador de respuesta, como R001, R002 o R003, sin vincularlo a datos identificativos.
2. Configurar el formulario para que no recopile direcciones de correo electrónico automáticamente.
3. Evitar solicitar nombres y otros identificadores directos.
4. Revisar los comentarios abiertos y eliminar referencias que permitan reconocer a una persona.
5. Guardar las respuestas en archivos CSV con las variables estrictamente necesarias.
6. Mantener cualquier archivo original que contenga información identificable fuera del repositorio público.
7. Publicar exclusivamente datos anonimizados y revisados.
8. Limitar el acceso a los archivos de trabajo a los integrantes autorizados del equipo.

**Consentimiento informado:**

Antes de iniciar la encuesta, se mostrará el siguiente texto:

> Esta encuesta se realiza con fines académicos para conocer la satisfacción y las expectativas de compradores de supermercados en Quito. Su participación es voluntaria y puede decidir no responder. No se solicitará información que permita identificarle directamente. Las respuestas serán analizadas de forma agrupada y podrán incorporarse de manera anonimizada al informe académico.

El consentimiento se solicitará antes de mostrar el cuestionario principal.

**Almacenamiento y publicación:**

Las respuestas sin anonimizar, si llegaran a existir, se almacenarán únicamente en un espacio privado con acceso restringido. Los archivos publicados en GitHub no deberán contener información que permita identificar directa o indirectamente a los participantes.

Los datos simulados se identificarán de forma explícita mediante la columna `origen`, mientras que los reales se registrarán con `origen = real`.

## 7. Verificación con herramientas (Python/R)

**Herramienta seleccionada:** Python 3 con la biblioteca pandas.

**Archivo:** `scripts/verificacion_encuesta.py`

El script tendrá como objetivo comprobar la estructura del CSV, detectar valores faltantes, verificar los tipos de datos y analizar las distribuciones de satisfacción y recomendación.

Además, permitirá separar respuestas reales y simuladas, evitando que los registros artificiales distorsionen la interpretación de los resultados.

### 7.1. Código de verificación

```python
from pathlib import Path
import pandas as pd

# TODO 1: Cargar el CSV con pandas
ruta = (
    Path(__file__).resolve().parent.parent
    / "plantillas"
    / "encuesta_respuestas.csv"
)

df = pd.read_csv(ruta)

print("=== AUDITORÍA DE ENCUESTA ===")
print("Registros:", len(df))
print("Columnas:", len(df.columns))

# TODO 2: Mostrar los dtypes
print("\n=== TIPOS DE DATOS ===")
print(df.dtypes)

# TODO 3: Mostrar los datos faltantes
print("\n=== DATOS FALTANTES ===")
print(df.isna().sum())

# TODO 4: Distribuciones generales
for columna in [
    "satisfaccion_general",
    "recomendaria"
]:
    print(f"\n=== {columna} ===")
    print(
        df[columna].value_counts(
            dropna=False
        ).sort_index()
    )

# Separar las respuestas reales de las simuladas
if "origen" in df.columns:
    reales = df.loc[
        df["origen"].astype(str).str.lower()
        == "real"
    ].copy()

    simuladas = df.loc[
        df["origen"].astype(str).str.lower()
        == "simulada"
    ].copy()

    print("\n=== ORIGEN DE LOS DATOS ===")
    print("Reales:", len(reales))
    print("Simuladas:", len(simuladas))
else:
    raise ValueError(
        "El CSV debe contener la columna origen"
    )

# Auditoría únicamente de registros reales
print("\n=== ANÁLISIS DE RESPUESTAS REALES ===")

if reales.empty:
    print("Aún no existen respuestas reales.")
else:
    for columna in [
        "satisfaccion_general",
        "recomendaria"
    ]:
        print(f"\n{columna}:")
        print(
            reales[columna].value_counts(
                dropna=False
            ).sort_index()
        )

    print("\nFaltantes en registros reales:")
    print(reales.isna().sum())

    print("\nPorcentaje de recomendación:")
    recomendacion = (
        reales["recomendaria"].eq("Si").mean()
        * 100
    )
    print(f"{recomendacion:.2f}%")

    print("\nSatisfacción favorable (4 o 5):")
    validas = pd.to_numeric(
        reales["satisfaccion_general"],
        errors="coerce"
    ).dropna()

    if len(validas) > 0:
        porcentaje = validas.ge(4).mean() * 100
        print(f"{porcentaje:.2f}%")
    else:
        print("Sin puntuaciones válidas")

    # Revisión de variables adicionales
    for columna in [
        "frecuencia_visita",
        "interes_programa",
        "beneficio_preferido",
        "aspecto_mejora"
    ]:
        if columna in reales.columns:
            print(f"\nDistribución de {columna}:")
            print(
                reales[columna].value_counts(
                    dropna=False
                )
            )

    # Comprobaciones de validez
    if "edad" in reales.columns:
        edad = pd.to_numeric(
            reales["edad"],
            errors="coerce"
        )
        print(
            "\nEdades inválidas:",
            (edad.lt(18) | edad.isna()).sum()
        )

    for columna in [
        "satisfaccion_general",
        "interes_programa"
    ]:
        if columna in reales.columns:
            valores = pd.to_numeric(
                reales[columna],
                errors="coerce"
            )
            invalidos = (
                ~valores.isin([1, 2, 3, 4, 5])
            ).sum()
            print(
                f"Valores inválidos en {columna}:",
                invalidos
            )

    # Posibles señales de sesgo
    print("\n=== INTERPRETACIÓN PRELIMINAR ===")
    print(
        "Una concentración de participantes "
        "en una sola categoría puede indicar "
        "un problema de cobertura."
    )
    print(
        "Una concentración extrema de "
        "respuestas positivas requiere "
        "revisar un posible sesgo de respuesta."
    )
    print(
        "El sesgo de no respuesta necesita "
        "también el registro de invitaciones "
        "y rechazos."
    )
```

### 7.2. Ejecución sobre el CSV de ejemplo

El CSV original del repositorio contiene cuatro filas ilustrativas, tres marcadas como reales y una como simulada.

Estas filas son únicamente ejemplos suministrados en la plantilla del laboratorio y no constituyen resultados recolectados por el Equipo 3.

Al ejecutar la auditoría sobre ese archivo se obtienen diez columnas:

| Columna | Dtype detectado | Faltantes |
|---|---|---:|
| `respuesta_id` | `object` | 0 |
| `fecha` | `object` | 0 |
| `ciudad` | `object` | 0 |
| `edad` | `int64` | 0 |
| `genero` | `object` | 0 |
| `frecuencia_visita` | `object` | 0 |
| `satisfaccion_general` | `int64` | 0 |
| `recomendaria` | `object` | 0 |
| `comentario` | `object` | 1 |
| `origen` | `object` | 0 |

**Distribución de satisfacción general, cuatro registros de ejemplo:**

| Satisfacción | Frecuencia |
|---|---:|
| 3 | 1 |
| 4 | 2 |
| 5 | 1 |

**Distribución de recomendación, cuatro registros de ejemplo:**

| Recomendación | Frecuencia |
|---|---:|
| Si | 3 |
| No | 1 |

**Separación por origen:**

| Origen | Registros |
|---|---:|
| real | 3 |
| simulada | 1 |

Los resultados anteriores únicamente demuestran el funcionamiento de la auditoría sobre datos ilustrativos.

### 7.3. ¿Coinciden los tipos con la predicción de la sección 4?

Sí, los campos compartidos entre el CSV original y el cuestionario propuesto presentan tipos coherentes con las predicciones.

Las columnas `edad` y `satisfaccion_general` se interpretan como `int64`, mientras que las variables categóricas almacenadas mediante etiquetas se interpretan como `object`.

En particular, la satisfacción se registra numéricamente pero sigue siendo una variable ordinal.

Las variables nuevas `interes_programa`, `beneficio_preferido` y `aspecto_mejora` deberán agregarse al CSV cuando se implemente el cuestionario definitivo. Sus tipos y valores se comprobarán después de aplicar la encuesta.

### 7.4. ¿Cuántos datos faltantes hay por columna?

En el CSV original de ejemplo se detecta un único dato faltante en la columna `comentario`. Las demás columnas presentan cero valores faltantes.

El campo `comentario` es opcional, por lo que la ausencia de un valor no constituye necesariamente un error de calidad. Es importante distinguir los datos no obligatorios de los datos requeridos para los indicadores principales.

### 7.5. Interpretación de los posibles sesgos

**Sesgo de selección:**

Una acumulación de participantes en un único grupo de edad o frecuencia de compra podría sugerir una cobertura limitada. Por ejemplo, una muestra compuesta casi exclusivamente por estudiantes universitarios no describiría adecuadamente la diversidad de compradores adultos de Quito.

**Sesgo de no respuesta:**

Para detectar este problema será necesario comparar las invitaciones realizadas con las encuestas válidas recibidas. Si un grupo de invitados responde significativamente menos que otro, podría existir un mecanismo de no respuesta asociado con sus características.

La presencia de celdas vacías también permitirá estudiar la no respuesta a preguntas específicas, pero no reemplaza el registro de las personas que nunca completaron el formulario.

**Sesgo de respuesta:**

Una distribución extremadamente concentrada en los valores más altos de satisfacción o en recomendaciones positivas podría justificar una revisión del instrumento y de las condiciones de aplicación. Esta concentración no demuestra por sí sola que exista sesgo.

**Interpretación de las filas reales del CSV de ejemplo:**

Al excluir la fila simulada, quedan tres registros ilustrativos con puntuaciones 3, 4 y 5, respectivamente. Dos de ellos incluyen recomendaciones afirmativas y uno una recomendación negativa.

El número de registros es demasiado pequeño y corresponde a datos de ejemplo. Por consiguiente, no se presentan conclusiones sobre los consumidores reales ni se atribuyen estos resultados al Equipo 3.

**Conclusión de la verificación:**

La auditoría permite comprobar que el CSV puede leerse correctamente, verificar los tipos de datos, identificar los valores faltantes y examinar las distribuciones solicitadas. La interpretación definitiva dependerá de las respuestas reales recolectadas y de la evaluación del procedimiento de muestreo.

---

## Conclusiones preliminares del diseño

1. El diseño de la encuesta establece una relación directa entre la satisfacción de los consumidores y las decisiones de la gerencia sobre programas de fidelización. Los indicadores definidos permiten obtener información descriptiva para identificar prioridades comerciales y oportunidades de mejora.

2. La combinación de un cuestionario estructurado, un muestreo declarado de forma transparente, medidas de confidencialidad y verificaciones mediante Python ofrece un procedimiento reproducible para el laboratorio. No obstante, las conclusiones deberán reconocer las limitaciones del muestreo por conveniencia y diferenciar estrictamente las respuestas reales de los registros simulados.

**Estado del trabajo:** Diseño propuesto. Pendientes de ejecución: aprobación del enfoque, aplicación de la encuesta, actualización del CSV y auditoría final con respuestas reales.
