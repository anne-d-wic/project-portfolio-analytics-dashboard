# Project Portfolio Analytics Dashboard

Power BI portfolio dashboard built with Python, Pandas, and DAX to analyze delivery performance, risk concentration, and corrective-action priorities across a simulated PMO portfolio.

## What This Project Demonstrates
This project shows how portfolio data can be generated, validated, enriched, modeled, and translated into a decision-support dashboard.

It highlights:
- KPI design for portfolio monitoring
- Python-based data preparation and enrichment
- star schema modeling in Power BI
- cross-page analysis for executive reporting

Business Questions Answered:
- Which programs are underperforming on delivery?
- Where is risk concentrated across the portfolio?
- Which projects should be prioritized for corrective action?

## Why This Project Matters
This dashboard is designed to support portfolio-level decision-making, not just project tracking.

It helps PMO analysts, portfolio managers, and program leaders:
- identify where delivery risk is concentrated
- isolate the main drivers of slippage
- compare execution performance across the portfolio
- prioritize corrective action more effectively

## Dashboard Pages
| Page | Purpose |
|---|---|
| Portfolio Overview | High-level view of portfolio health, status distribution, and issue concentration |
| Delivery Performance | Execution trends, schedule slippage, and underperforming areas |
| Risk Analysis | Risk exposure, severity, and drivers of delivery pressure |

## Screenshots

### Portfolio Overview
![Portfolio Overview](/images/portfolio_overview.png)

### Delivery Performance
![Delivery Performance](/images/delivery_performance.png)

### Risk Analysis
![Risk Analysis](/images/risk_analysis.png)

## Tools & Skills
### Tools Used
- Power BI (data visualization)
- DAX (measures)
- Python (data generation & preprocessing)
- Pandas (data transformation)
- GitHub (versioning & portfolio)

### Skills Demonstrated
- KPI design for portfolio management
- Power BI dashboard development
- Star schema modeling
- Business-oriented data storytelling
- Python-based data preparation
- Risk and delivery performance analysis

## Dashboard Navigation and Cross-Page Analysis
<details><summary><strong>See more</strong></summary>
  
The report is designed as a connected analytical workflow rather than a set of isolated pages. Each page addresses a different portfolio management question, while shared filters preserve the same analytical scope across the dashboard.
Users can begin with a high-level portfolio view, move to delivery execution analysis, and then examine risk concentration without losing context.

### How the Pages Connect
- Portfolio Overview provides the overall picture of portfolio health, project status, and concentration of issues
- Delivery Performance focuses on execution trends, schedule slippage, and delivery performance across projects or programs
- Risk Analysis highlights risk exposure, severity, and the main sources of delivery pressure

Together, these pages support a progression from summary to diagnosis:

- Portfolio Overview identifies where attention is needed
- Delivery Performance explains where execution is deteriorating
- Risk Analysis helps clarify the underlying exposure behind underperforming projects

### Shared Filters Across Pages
The dashboard uses shared slicers to maintain a consistent decision perimeter across pages.

Common filters may include:

- reporting period
- project status
- program or portfolio segment
- business area
- risk level

When a user applies a filter on one page, that context is preserved while navigating to the others. As a result:

- visuals remain aligned on the same subset of projects
- KPI comparisons stay consistent across report pages
- users can move from summary to detail without resetting their analysis

Page-level filters may still be used for more focused exploration, but the global filter context remains the main analytical backbone of the report.

### Example Analytical Flow
A portfolio manager may start on Portfolio Overview to isolate projects marked as At Risk. From there, they can move to Delivery Performance to determine whether delays are concentrated in specific programs or milestone phases. They can then open Risk Analysis to assess whether those same projects also carry elevated risk exposure. Because the filter context is preserved across pages, the analysis remains coherent from overview to root-cause investigation.
</details>

## Business Context and Objective
<details><summary><strong>See more</strong></summary>
  
This project was designed as a portfolio management decision-support dashboard for a PMO or transformation office overseeing multiple programs and projects.
The objective is not only to track project status, but to identify where delivery risk is concentrated, which programs require escalation and which project phases contribute most to delays.

### Objective
Build a Power BI dashboard that helps decision-makers answer three critical questions:
1. Which programs are underperforming on delivery?
2. Where is risk concentrated across the portfolio?
3. Which projects and milestone phases should be prioritized for corrective action?

### What Makes This Useful for Decision-Makers
This dashboard is designed to support portfolio-level decision-making, not just project tracking. It helps PMO analysts, portfolio managers and program leaders quickly identify where delivery risk is concentrated, which programs require escalation, and which projects or milestone phases should be prioritized for corrective action.
By combining delivery, budget and risk indicators in one model, the dashboard makes it easier to move from reporting to action.

### Target Audience
- PMO analysts
- Portfolio managers
- Program directors
- Transformation leaders

### Analytical Scope
The dashboard covers three complementary dimensions of portfolio performance:
- Delivery performance
- Risk exposure
- Budget and delay impact
</details>

## Key KPIs
<details><summary><strong>See more</strong></summary>

- On-time delivery rate: share of projects delivered on or before target date
- Budget variance: difference between actual and planned budget
- Delay impact: cumulative delay generated by late projects
- High-risk project ratio: share of projects flagged as high risk
- Top delay contributors: projects accounting for the largest share of total delay impact
  </details>

## Data Model
<details><summary><strong>See more</strong></summary>

The model follows a star schema structure (fact & dimension tables), supporting KPI consistency, scalable filtering and drill-down analysis.

The dashboard relies on a relational model connecting projects, milestones, risks, and resources to support portfolio-level analysis.

![Page 4](images/data_model.png)
</details>

## Data Preparation Workflow
<details><summary><strong>See more</strong></summary>
  
1. Generate realistic portfolio data using Python
2. Run sanity checks across projects, milestones and risks
3. Enrich the datasets for reporting use cases
4. Build the data model in Power BI
5. Design KPI-driven dashboard pages for executive and operational analysis

### How the Data Is Rebuilt
The reporting datasets used in this dashboard are rebuilt through a three-step Python workflow. The first script generates a realistic portfolio dataset, the second script validates consistency rules across the generated files, and the third script enriches the datasets with reporting-oriented fields used in the Power BI model.
This approach makes the project reproducible and shows how raw simulated data can be turned into structured, analysis-ready inputs for portfolio reporting.

### Transformation Logic
Python is used to move the project from raw simulated records to analysis-ready reporting tables. This includes generating base entities, checking consistency across projects, milestones and risks, and enriching the data with fields that support KPI calculation, filtering and business interpretation in Power BI.
The transformation flow can be summarized as follows: simulated source data -> sanity checks -> enriched reporting tables -> Power BI model -> dashboard analysis.
</details>

## Business Assumptions
<details><summary><strong>See more</strong></summary>
  
This project relies on a set of business assumptions designed to simulate a realistic PMO reporting environment. These assumptions include project status classification, milestone delay logic, budget variance calculation, and risk scoring rules used to flag high-risk projects.
The objective is not to replicate a specific company's methodology, but to demonstrate how analytical rules can be structured to support portfolio-level monitoring, prioritization and escalation.
</details>

## Key Insights
<details><summary><strong>See more</strong></summary>

The dashboard is designed to support a portfolio-level reading of delivery performance rather than a purely descriptive project review. The main value of the analysis comes from identifying where execution pressure, delay concentration, and risk exposure intersect.

The report is intended to help surface insights such as:

- which parts of the portfolio concentrate the highest proportion of projects under pressure
- whether delivery slippage appears isolated or systemic across programs
- which at-risk projects combine weak delivery performance with elevated risk exposure
- where portfolio managers may need to prioritize escalation or corrective action

Taken together, these insights help shift the dashboard from status reporting to management support. Instead of only showing that some projects are delayed or risky, the report helps explain where attention should be focused and why those areas matter at portfolio level.
</details>

## Recommendations
<details><summary><strong>See more</strong></summary>
  
- Prioritize corrective action on the top delayed projects rather than spreading attention evenly across the portfolio.
- Review milestone governance in Planning and Testing phases to reduce repeated execution bottlenecks.
- Use targeted program reviews for underperforming areas instead of portfolio-wide generic escalation.
- Track delivery and risk indicators together to anticipate execution slippage earlier.
</details>

## Reproducibility
<details><summary><strong>See more</strong></summary>

The project can be reproduced from the Python scripts and CSV outputs included in this repository.
  
### Steps
1. Run `1_generate_portfolio_data.py` to generate the base portfolio datasets
2. Run `2_sanity_checks.py` to validate data consistency across projects, milestones and risks
3. Run `3_enrich_data.py` to create reporting-ready datasets for the dashboard
4. Open the Power BI file and connect it to the generated files in the `data/` folder
### Output Files
The workflow produces and updates CSV files in the `data/` folder, including project, milestone, risk and resource datasets used in the final model.
### Notes
The data used in this project is simulated for demonstration purposes. The goal is to showcase analytical reasoning, KPI design, data preparation and dashboard storytelling in a realistic PMO reporting scenario.
### Requirements
- Python 3.x
- pandas
- Power BI Desktop
- Access to the files stored in the `data/` folder
</details>

## Project Structure
<details><summary><strong>See more</strong></summary>
  
- /dashboard -> Power BI file (.pbix)
- /data -> CSV datasets
- /analysis -> Python scripts
- /images -> dashboard & data model screenshots
</details>

## Notes
<details><summary><strong>See more</strong></summary>
  
The data used in this project is simulated for demonstration purposes.

The emphasis is on analytical reasoning, KPI design, transformation logic, dashboard structure, and business-oriented interpretation in a realistic PMO reporting scenario.
</details>
