-- Least-privilege grants aligned to enterprise banking controls.
GRANT USE CATALOG ON CATALOG finance TO `finance_engineers`;
GRANT USE CATALOG ON CATALOG finance TO `finance_analysts`;
GRANT USE CATALOG ON CATALOG finance TO `risk_analysts`;

GRANT USE SCHEMA ON SCHEMA finance.silver TO `finance_engineers`;
GRANT SELECT ON ALL TABLES IN SCHEMA finance.silver TO `finance_engineers`;

GRANT USE SCHEMA ON SCHEMA finance.gold TO `finance_analysts`;
GRANT SELECT ON ALL TABLES IN SCHEMA finance.gold TO `finance_analysts`;

GRANT USE SCHEMA ON SCHEMA finance.gold TO `risk_analysts`;
GRANT SELECT ON TABLE finance.gold.finance_daily_summary TO `risk_analysts`;

-- No direct Bronze access granted to analyst personas.
