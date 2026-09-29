import duckdb
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

con = duckdb.connect(r'C:\Users\annew\Documents\ANIA\Formations\project-portfolio-analytics-dashboard\data\portfolio.duckdb', read_only=True)

projects_enriched = con.sql("select * from main_intermediate.int_projects").df()
projects_enriched = projects_enriched.rename(columns={
    "project_id": "ProjectID",
    "project_name": "ProjectName",
    "program": "Program",
    "start_date":"StartDate",
    "end_date": "EndDate",
    "budget": "Budget",
    "actual_cost": "ActualCost",
    "status": "Status",
    "priority": "Priority",
    "sponsor": "Sponsor",
    "budget_variance": "BudgetVariance",
    "budget_variance_pct": "BudgetVariancePct",
    "project_duration_days": "ProjectDurationDays",
    "is_delayed": "IsDelayed"
})

milestones_enriched = con.sql("select * from main_intermediate.int_milestones_detail").df()
milestones_enriched = milestones_enriched.rename(columns={
    "milestone_id": "MilestoneID",
    "project_id": "ProjectID",
    "milestone_name": "MilestoneName",
    "planned_date": "PlannedDate",
    "actual_date": "ActualDate",
    "delay_days": "DelayDays",
    "is_delayed_milestone": "IsDelayedMilestone"
})

risks_enriched = con.sql("select * from main_intermediate.int_risks_detail").df()
risks_enriched = risks_enriched.rename(columns={
    "risk_id": "RiskID",
    "project_id": "ProjectID",
    "risk_level": "RiskLevel",
    "impact": "Impact",
    "probability": "Probability",
    "status": "Status",
    "risk_score": "RiskScore",
    "is_high_risk": "IsHighRisk"
})

resources = con.sql("select * from main_staging.stg_resources").df()
resources = resources.rename(columns={
    "resource_id": "ResourceID",
    "project_id": "ProjectID",
    "role": "Role",
    "allocation_pct": "AllocationPct",
    "cost": "Cost"
})
