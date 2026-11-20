# comparacion_experimento.py — Comparación de grupos y asignación aleatoria (Python)
# Ejecuta desde la raíz del repositorio:
#   python scripts/comparacion_experimento.py
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# PARTE A — Comparación sobre la plantilla de registro (sección 9)
# ---------------------------------------------------------------------------

# TODO 1: carga plantillas/registro_experimento.csv con pandas
df = pd.read_csv("plantillas/registro_experimento.csv")
print(df.head())
print("*" * 5)

# TODO 2: promedio de ventas_producto por ubicacion
promedio = df.groupby("ubicacion")["ventas_producto"].mean()
print(promedio)
print("*" * 5)

# TODO 3: número de registros por grupo
print(df["ubicacion"].value_counts())
print("*" * 5)

# TODO 4: interpretación
# Con 4 filas (2 por grupo), cada tienda aparece una sola vez y en una sola
# condición: la diferencia puede deberse a la ciudad, al tamaño de la tienda o a
# la promoción simultánea (Guayaquil Centro tenía una). No hay asignación al
# azar ni medida de variabilidad, así que el promedio solo describe esas 4 filas.
print("Interpretación: con 4 filas el promedio por grupo es descriptivo; no prueba efecto.")
print("*" * 5)

# ---------------------------------------------------------------------------
# PARTE B — Asignación aleatoria del diseño (sección 5)
# Diseño: cruzado (crossover) dentro de cada tienda, alternando la ubicación
# cada semana. Lo que se sortea es con qué condición EMPIEZA cada tienda.
# ---------------------------------------------------------------------------
tiendas = ["Quito Norte", "Quito Sur", "Guayaquil Centro", "Guayaquil Norte",
           "Cuenca Centro", "Cuenca Sur", "Ambato Centro", "Manta", "Loja",
           "Machala"]
semanas = [1, 2, 3, 4]

rng = np.random.default_rng(2026)  # semilla fija: la corrida se puede repetir

# Línea de asignación: 5 tiendas empiezan en pasillo_principal y 5 en habitual,
# repartidas al azar (la mitad y la mitad, para que los grupos queden balanceados)
inicio = rng.permutation(["pasillo_principal"] * 5 + ["habitual"] * 5)

filas = []
for tienda, cond in zip(tiendas, inicio):
    otra = "habitual" if cond == "pasillo_principal" else "pasillo_principal"
    for s in semanas:
        filas.append({"tienda": tienda, "semana": s,
                      "ubicacion": cond if s % 2 == 1 else otra})

asignacion = pd.DataFrame(filas)
print(asignacion.pivot(index="tienda", columns="semana", values="ubicacion")
      .loc[tiendas])
print(asignacion["ubicacion"].value_counts())
