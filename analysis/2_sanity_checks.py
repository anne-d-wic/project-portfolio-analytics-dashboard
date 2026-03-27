import pandas as pd

# Load datasets
projects = pd.read_csv("data/projects.csv")
milestones = pd.read_csv("data/milestones.csv")
risks = pd.read_csv("data/risks.csv")
resources = pd.read_csv("data/resources.csv")

print("=== DATASET SHAPES ===")
print("Projects:", projects.shape)
print("Milestones:", milestones.shape)
print("Risks:", risks.shape)
print("Resources:", resources.shape)

print("\n=== MISSING VALUES ===")
print("\nProjects")
print(projects.isnull().sum())
print("\nMilestones")
print(milestones.isnull().sum())
print("\nRisks")
print(risks.isnull().sum())
print("\nResources")
print(resources.isnull().sum())

print("\n=== DUPLICATE KEYS ===")
print("Duplicate ProjectID:", projects["ProjectID"].duplicated().sum())
print("Duplicate MilestoneID:", milestones["MilestoneID"].duplicated().sum())
print("Duplicate RiskID:", risks["RiskID"].duplicated().sum())
print("Duplicate ResourceID:", resources["ResourceID"].duplicated().sum())

print("\n=== REFERENTIAL INTEGRITY ===")
project_ids = set(projects["ProjectID"])

print("Milestones with unknown ProjectID:",
      (~milestones["ProjectID"].isin(project_ids)).sum())

print("Risks with unknown ProjectID:",
      (~risks["ProjectID"].isin(project_ids)).sum())

print("Resources with unknown ProjectID:",
      (~resources["ProjectID"].isin(project_ids)).sum())

print("\n=== PROJECT STATUS DISTRIBUTION ===")
print(projects["Status"].value_counts())

print("\n=== PROJECT PRIORITY DISTRIBUTION ===")
print(projects["Priority"].value_counts())

print("\n=== RISK LEVEL DISTRIBUTION ===")
print(risks["RiskLevel"].value_counts())

print("\n=== BUDGET CHECK ===")
print(projects[["Budget", "ActualCost"]].describe())

over_budget = (projects["ActualCost"] > projects["Budget"]).sum()
print("Projects over budget:", over_budget)

print("\n=== DATE CHECKS ===")
projects["StartDate"] = pd.to_datetime(projects["StartDate"])
projects["EndDate"] = pd.to_datetime(projects["EndDate"])
milestones["PlannedDate"] = pd.to_datetime(milestones["PlannedDate"])
milestones["ActualDate"] = pd.to_datetime(milestones["ActualDate"])

print("Start Date Range :")
print(projects["StartDate"].min(), projects["StartDate"].max())
print("End Date Range :")
print(projects["EndDate"].min(), projects["EndDate"].max())

invalid_project_dates = (projects["EndDate"] < projects["StartDate"]).sum()
print("Projects with EndDate before StartDate:", invalid_project_dates)

invalid_milestone_dates = (milestones["ActualDate"] < milestones["PlannedDate"]).sum()
print("Milestones with ActualDate before PlannedDate:", invalid_milestone_dates)

negative_delays = (milestones["DelayDays"] < 0).sum()
print("Milestones with negative DelayDays:", negative_delays)

print("\n=== STATUS VS DELAY LOGIC ===")
delayed_projects = projects[projects["Status"] == "Delayed"]["ProjectID"]
milestones_delayed = milestones[milestones["ProjectID"].isin(delayed_projects)]

print("Average milestone delay for delayed projects:",
      milestones_delayed["DelayDays"].mean())

ontrack_projects = projects[projects["Status"] == "On Track"]["ProjectID"]
milestones_ontrack = milestones[milestones["ProjectID"].isin(ontrack_projects)]

print("Average milestone delay for on-track projects:",
      milestones_ontrack["DelayDays"].mean())

print("\n=== STATUS VS RISK LOGIC ===")
atrisk_projects = projects[projects["Status"] == "At Risk"]["ProjectID"]
risks_atrisk = risks[risks["ProjectID"].isin(atrisk_projects)]

print("Average impact for at-risk projects:",
      risks_atrisk["Impact"].mean())

print("Average probability for at-risk projects:",
      risks_atrisk["Probability"].mean())

print("\n=== RESOURCE CHECK ===")
print(resources[["AllocationPct", "Cost"]].describe())

invalid_alloc = ((resources["AllocationPct"] < 0) | (resources["AllocationPct"] > 100)).sum()
print("Resources with invalid allocation %:", invalid_alloc)

print("\n=== PROGRAM DISTRIBUTION ===")
print(projects["Program"].value_counts())

print("\nSanity checks completed.")