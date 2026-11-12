# Databricks notebook source
catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")
ruta = f"/Volumes/{catalog}/{schema}/raw/pedidos.csv"

spark.sql(f"USE CATALOG `{catalog}`")
spark.sql(f"USE SCHEMA `{schema}`")

# COMMAND ----------

df = spark.read.option("header", True).option("inferSchema", True).csv(ruta)
df.write.mode("overwrite").saveAsTable("pedidos")
print(df.count(), "filas cargadas")