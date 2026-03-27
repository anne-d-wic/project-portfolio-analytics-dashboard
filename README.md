# project-portfolio-analytics-dashboard
Power BI dashboard analyzing project portfolio performance, delivery efficiency, and risk exposure with a business-oriented approach.

## Overview

This project showcases a Power BI dashboard designed to analyze project portfolio performance across delivery, risk, and financial dimensions.

The dashboard is structured into three main analytical layers:
- Portfolio overview
- Risk analysis
- Delivery performance

---

## Key Features

- KPI-driven analysis (on-time rate, budget variance, delay impact)
- Program-level performance comparison
- Identification of most delayed projects
- Root cause analysis through milestone phases
- Fully interactive filtering (date, program, risk level, etc.)

---

## Data Model

The data model follows a star schema design:
- Fact tables: Projects, Milestones, Risks
- Dimension tables: Date, Program, Phase, Status

---

## Tools & Technologies

- Power BI (data visualization)
- Python (data generation & preprocessing)
- Pandas (data transformation)
- GitHub (versioning & portfolio)

---

## Project Structure

- `/dashboard` → Power BI file (.pbix)
- `/data` → CSV datasets
- `/analysis` → Python scripts
- `/images` → dashboard screenshots

---

## Dashboard Preview

### Page 1 — Portfolio Overview
![Page 1](images/portfolio_overview.png)

### Page 2 — Risk Analysis
![Page 2](images/risk_analysis.png)

### Page 3 — Delivery Performance
![Page 3](images/delivery_performance.png)

---

## Key Insights

- Delivery performance is uneven across programs, with Program C performing significantly below the portfolio average in terms of on-time delivery
- Approximately one-third of projects drive the majority of total delay, indicating a strong concentration of delivery risk
- Testing and Planning phases contribute disproportionately to overall delays, suggesting potential bottlenecks in execution readiness and validation processes
- The top 10 delayed projects account for a significant share of total delay impact, highlighting clear prioritization opportunities
- Budget performance remains relatively stable compared to delivery performance, suggesting that delays are driven more by operational challenges than financial constraints

---

## How to Use

1. Open the `.pbix` file in Power BI Desktop
2. Refresh data if needed
3. Use slicers to explore the portfolio

---

## Author

Data Analyst transitioning into advanced analytics with a focus on business-driven insights and decision support.
