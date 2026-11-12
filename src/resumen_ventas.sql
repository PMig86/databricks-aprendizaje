-- Databricks notebook source
USE CATALOG IDENTIFIER(:catalog);
USE SCHEMA IDENTIFIER(:schema);

-- COMMAND ----------

CREATE OR REPLACE TABLE ventas_mensuales AS
SELECT date_format(fecha, 'yyyy-MM') AS mes,
       ciudad,
       SUM(cantidad * precio_unitario) AS ventas,
       COUNT(*) AS pedidos
FROM pedidos
GROUP BY 1, 2;