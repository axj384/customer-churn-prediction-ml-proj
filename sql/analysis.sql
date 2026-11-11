-- SQLite table: customers
SELECT contract_type, COUNT(*) AS customers, ROUND(AVG(churned)*100,1) AS churn_rate_pct FROM customers GROUP BY contract_type;
SELECT CASE WHEN tenure_months<12 THEN '0-11' WHEN tenure_months<36 THEN '12-35' ELSE '36+' END AS tenure_band, COUNT(*) AS customers, ROUND(AVG(churned)*100,1) AS churn_rate_pct FROM customers GROUP BY tenure_band;
SELECT autopay, ROUND(AVG(churned)*100,1) AS churn_rate_pct FROM customers GROUP BY autopay;
