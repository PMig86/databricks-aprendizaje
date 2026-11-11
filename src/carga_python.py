# Databricks notebook source
catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")

spark.sql(f"USE CATALOG `{catalog}`")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS `{schema}`")
spark.sql(f"USE SCHEMA `{schema}`")

# COMMAND ----------

datos = [
    ("2026-01", "Quito", 1200.0),
    ("2026-01", "Guayaquil", 1850.5),
    ("2026-02", "Quito", 1430.0),
    ("2026-02", "Guayaquil", 1710.0),
    ("2026-03", "Quito", 1580.25),
    ("2026-03", "Guayaquil", 2010.0),
]
df = spark.createDataFrame(datos, ["mes", "ciudad", "ventas"])
df.write.mode("overwrite").saveAsTable("ventas_python")

# COMMAND ----------

display(spark.table("ventas_python"))