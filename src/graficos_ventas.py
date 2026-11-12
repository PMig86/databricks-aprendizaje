# Databricks notebook source
# MAGIC %md
# MAGIC # Gráficos de ventas
# MAGIC Dos gráficos con matplotlib sobre las tablas del pipeline.

# COMMAND ----------

import matplotlib.pyplot as plt

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")
spark.sql(f"USE CATALOG `{catalog}`")
spark.sql(f"USE SCHEMA `{schema}`")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ventas mensuales por ciudad

# COMMAND ----------

pdf = spark.table("ventas_mensuales").toPandas()
pivot = pdf.pivot_table(index="mes", columns="ciudad", values="ventas", aggfunc="sum").sort_index()

ax = pivot.plot(kind="line", marker="o", figsize=(10, 5))
ax.set_title("Ventas mensuales por ciudad")
ax.set_xlabel("Mes")
ax.set_ylabel("Ventas (USD)")
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ventas totales por producto

# COMMAND ----------

por_producto = spark.sql("""
    SELECT producto, SUM(cantidad * precio_unitario) AS ventas
    FROM pedidos GROUP BY producto ORDER BY ventas DESC
""").toPandas()

ax = por_producto.plot(kind="bar", x="producto", y="ventas", legend=False, figsize=(8, 5))
ax.set_title("Ventas totales por producto")
ax.set_ylabel("Ventas (USD)")
plt.show()

# COMMAND ----------

# Alternativa nativa: display() permite crear gráficos con el botón "+" de la tabla
display(spark.table("ventas_mensuales").orderBy("mes", "ciudad"))