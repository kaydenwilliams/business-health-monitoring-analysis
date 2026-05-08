CREATE OR REPLACE VIEW business_health_kpis AS
WITH lagged_values AS (
	SELECT date, 
		series_id, 
        value, 
		LAG(value, 1) OVER (PARTITION BY series_id ORDER BY date) AS prev_month_value,
        LAG(value, 12) OVER (PARTITION BY series_id ORDER BY date) AS prev_year_value
	FROM economic_indicators
)
SELECT *, 
    ROUND(value - prev_month_value, 2) AS mom_change,
    ROUND(value - prev_year_value, 2) AS yoy_change
FROM lagged_values
WHERE date >= DATE_SUB((SELECT MAX(date) FROM economic_indicators), INTERVAL 24 MONTH)