-- Databricks notebook source
USE CATALOG IDENTIFIER(:catalog);

-- COMMAND ----------

CREATE SCHEMA IF NOT EXISTS IDENTIFIER(:schema);
USE SCHEMA IDENTIFIER(:schema);

-- COMMAND ----------

CREATE OR REPLACE TABLE ventas_sql AS
SELECT * FROM VALUES
  ('2026-01', 'Quito', 1200.0),
  ('2026-01', 'Guayaquil', 1850.5),
  ('2026-02', 'Quito', 1430.0),
  ('2026-02', 'Guayaquil', 1710.0),
  ('2026-03', 'Quito', 1580.25),
  ('2026-03', 'Guayaquil', 2010.0)
AS t(mes, ciudad, ventas);

-- COMMAND ----------

SELECT * FROM ventas_sql;