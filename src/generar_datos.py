# Databricks notebook source
# MAGIC %md
# MAGIC # Generar datos ficticios de pedidos
# MAGIC Crea 5000 pedidos sintéticos y los guarda como CSV en un volume.

# COMMAND ----------

import csv
import random
from datetime import date, timedelta

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")

spark.sql(f"CREATE SCHEMA IF NOT EXISTS `{catalog}`.`{schema}`")
spark.sql(f"CREATE VOLUME IF NOT EXISTS `{catalog}`.`{schema}`.raw")
ruta = f"/Volumes/{catalog}/{schema}/raw/pedidos.csv"

# COMMAND ----------

random.seed(42)  # misma semilla = mismos datos en cada ejecución
ciudades = ["Quito", "Guayaquil", "Cuenca", "Ambato", "Manta"]
precios_base = {"Laptop": 900, "Monitor": 220, "Teclado": 35, "Mouse": 18, "Auricular": 60}
inicio = date(2026, 1, 1)

with open(ruta, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["pedido_id", "fecha", "ciudad", "producto", "cantidad", "precio_unitario"])
    for i in range(1, 5001):
        producto = random.choice(list(precios_base))
        w.writerow([
            i,
            (inicio + timedelta(days=random.randint(0, 299))).isoformat(),
            random.choice(ciudades),
            producto,
            random.randint(1, 5),
            round(precios_base[producto] * random.uniform(0.9, 1.1), 2),
        ])
print("CSV escrito en", ruta)