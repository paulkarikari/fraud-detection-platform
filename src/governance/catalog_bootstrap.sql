-- Unity Catalog bootstrap for finance domain.
CREATE CATALOG IF NOT EXISTS finance;

CREATE SCHEMA IF NOT EXISTS finance.bronze;
CREATE SCHEMA IF NOT EXISTS finance.silver;
CREATE SCHEMA IF NOT EXISTS finance.gold;
CREATE SCHEMA IF NOT EXISTS finance.audit;
