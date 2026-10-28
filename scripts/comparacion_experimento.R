# comparacion_experimento.R — Comparación de grupos (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/comparacion_experimento.R

# TODO 1: carga plantillas/registro_experimento.csv (read.csv)
import pandas as pd

df = pd.read_csv("registro_experimento.csv")

print(df.head())
# TODO 2: calcula e imprime el promedio de ventas_producto por ubicacion
#         (aggregate)

df.groupby("ubicacion")["ventas_producto"].mean()
# TODO 3: imprime el número de registros por grupo (table)

# TODO 4: escribe 2–3 líneas de interpretación (sección 9 de la plantilla):
#         por qué con 4 filas no se puede concluir y qué le faltaría al análisis

import pandas as pd
import numpy as np

tiendas = ["Quito Norte", "Quito Sur","Guayaquil Centro","Guayaquil Norte", "Cuenca Centro", "Cuenca Sur"
          "Ambato Centro", "Manta", "Loja","Machala"]

semanas =[1,2,3,4]

#Sorteo de la condicion inicial

rng = np.random.default_rng(1234597)
primera =rng.choice(["pasillo_principal","habitual"],size=len(tiendas))

filas=[]

for tiendas, cond in zip(tiendas,primera):
  otra = "habitual" if cond == "pasillo_principal" else "pasillo_principal"
  for s in semanas:
    filas.append({"tienda": tienda ,"semana": s, "condicion": cond if s%2 == 1 else otra})
