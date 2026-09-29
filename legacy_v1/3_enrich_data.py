import pandas as pd
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Load datasets
projects = pd.read_csv(REPO_ROOT / "data" / "projects.csv")
milestones = pd.read_csv(REPO_ROOT / "data" / "milestones.csv")
risks = pd.read_csv(REPO_ROOT / "data" / "risks.csv")

# Convert dates
projects["StartDate"] = pd.to_datetime(projects["StartDate"])
projects["EndDate"] = pd.to_datetime(projects["EndDate"])

milestones["PlannedDate"] = pd.to_datetime(milestones["PlannedDate"])
milestones["ActualDate"] = pd.to_datetime(milestones["ActualDate"])

# =========================
# PROJECTS ENRICHMENT
# =========================

# Budget variance
projects["BudgetVariance"] = projects["ActualCost"] - projects["Budget"]

# Budget variance %
projects["BudgetVariancePct"] = projects["BudgetVariance"] / projects["Budget"]

# Project duration
projects["ProjectDurationDays"] = (projects["EndDate"] - projects["StartDate"]).dt.days

# Delay flag
projects["IsDelayed"] = (projects["Status"] == "Delayed").astype(int)

# =========================
# RISKS ENRICHMENT
# =========================

# Risk score
risks["RiskScore"] = risks["Impact"] * risks["Probability"]

# High risk flag
risks["IsHighRisk"] = (risks["RiskLevel"] == "High").astype(int)

# =========================
# MILESTONES ENRICHMENT
# =========================

# Delay flag
milestones["IsDelayedMilestone"] = (milestones["DelayDays"] > 0).astype(int)

# =========================
# SAVE FILES
# =========================

projects.to_csv(REPO_ROOT / "data" / "projects_enriched.csv", index=False)
risks.to_csv(REPO_ROOT / "data" / "risks_enriched.csv", index=False)
milestones.to_csv(REPO_ROOT / "data" / "milestones_enriched.csv", index=False)

print("Data enrichment completed successfully.")