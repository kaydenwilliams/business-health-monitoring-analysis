# U.S. Business Health Monitor

## Overview
An automated economic intelligence pipeline that pulls live data from the Federal Reserve (FRED API), loads it into MySQL, calculates KPIs using SQL window functions, and surfaces the results in a Tableau dashboard updated on a daily schedule via cron job.

## Business Problem
Business decisions are affected by macroeconomic conditions — labor markets, inflation, and consumer confidence. This pipeline monitors three key U.S. economic indicators in near real time so analysts and decision makers can track trends without manually pulling data.

## Tools & Stack
Python, requests, pandas, SQLAlchemy, MySQL, SQL window functions, Tableau, cron scheduling, FRED API

## Pipeline Architecture
FRED API → Python (extract.py) → MySQL (economic_indicators table) → SQL view (business_health_kpis) → Tableau dashboard → cron job runs daily at 8am weekdays

## KPIs Monitored
- Unemployment Rate (UNRATE) — Bureau of Labor Statistics via FRED
- Consumer Price Index (CPIAUCSL) — inflation measure via FRED  
- Consumer Sentiment (UMCSENT) — University of Michigan survey via FRED

## Key Findings (as of May 2026)
- Unemployment has risen gradually from 3.9% to 4.3% over 24 months — a softening labor market
- CPI has climbed steadily from 312 to 330.3 — consistent inflation pressure with a 10.5 point year-over-year increase
- Consumer sentiment has dropped sharply from 79 to 53.3 — a 32% decline indicating significant deterioration in consumer confidence

## File Structure
business-health-monitoring-analysis/
├── extract.py
├── transform.sql
├── config.py (excluded from repo)
├── data/
│   └── business_health_kpis.csv
├── pipeline_log.txt
├── executive_summary.pdf
└── README.md
