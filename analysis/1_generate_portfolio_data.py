import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)

# --- PARAMETERS ---
num_projects = 40
programs = ["Program A", "Program B", "Program C", "Program D"]
statuses = ["On Track", "At Risk", "Delayed"]
priorities = ["Low", "Medium", "High"]
sponsors = ["IT", "Finance", "Operations", "HR"]

start_date = datetime(2025, 1, 1)

projects = []

for i in range(1, num_projects + 1):
    project_id = f"P{i:03}"
    program = random.choice(programs)
    priority = random.choice(priorities)
    status = random.choices(
        statuses,
        weights=[0.5, 0.3, 0.2]
    )[0]

    duration_days = random.randint(60, 180)
    project_start = start_date + timedelta(days=random.randint(0, 330))
    project_end = project_start + timedelta(days=duration_days)

    base_budget = random.randint(50000, 500000)

    if priority == "High":
        base_budget *= 1.5

    if status == "Delayed":
        actual_cost = base_budget * random.uniform(1.1, 1.4)
    elif status == "At Risk":
        actual_cost = base_budget * random.uniform(1.0, 1.2)
    else:
        actual_cost = base_budget * random.uniform(0.9, 1.05)

    projects.append([
        project_id,
        f"Project {i}",
        program,
        project_start,
        project_end,
        round(base_budget, 0),
        round(actual_cost, 0),
        status,
        priority,
        random.choice(sponsors)
    ])

projects_df = pd.DataFrame(projects, columns=[
    "ProjectID", "ProjectName", "Program", "StartDate", "EndDate",
    "Budget", "ActualCost", "Status", "Priority", "Sponsor"
])

projects_df.to_csv("data/projects.csv", index=False)

# --- MILESTONES ---
milestones = []
milestone_counter = 1

for _, row in projects_df.iterrows():
    num_milestones = random.randint(3, 6)

    for m in range(num_milestones):
        planned_date = row["StartDate"] + timedelta(days=random.randint(10, 150))

        delay = 0
        if row["Status"] == "Delayed":
            delay = random.randint(5, 30)
        elif row["Status"] == "At Risk":
            delay = random.randint(0, 15)

        actual_date = planned_date + timedelta(days=delay)

        milestone_id = f"M{milestone_counter:04}"

        milestones.append([
            milestone_id,
            row["ProjectID"],
            f"Milestone {m+1}",
            planned_date,
            actual_date,
            delay
        ])

        milestone_counter += 1

milestones_df = pd.DataFrame(milestones, columns=[
    "MilestoneID", "ProjectID", "MilestoneName", "PlannedDate", "ActualDate", "DelayDays"
])

milestones_df.to_csv("data/milestones.csv", index=False)

# --- RISKS ---
risks = []
risk_counter = 1

for _, row in projects_df.iterrows():
    num_risks = random.randint(2, 6)

    for _ in range(num_risks):
        if row["Status"] == "At Risk":
            impact = random.randint(3, 5)
            probability = random.randint(3, 5)
        else:
            impact = random.randint(1, 4)
            probability = random.randint(1, 4)

        risk_level = "High" if impact * probability > 12 else "Medium" if impact * probability > 6 else "Low"

        risk_id = f"R{risk_counter:04}"

        risks.append([
            risk_id,
            row["ProjectID"],
            risk_level,
            impact,
            probability,
            random.choice(["Open", "Mitigated", "Closed"])
        ])

        risk_counter += 1

risks_df = pd.DataFrame(risks, columns=[
    "RiskID", "ProjectID", "RiskLevel", "Impact", "Probability", "Status"
])

risks_df.to_csv("data/risks.csv", index=False)

# --- RESOURCES ---
roles = ["Developer", "Manager", "Analyst", "Engineer"]

resources = []
resource_counter = 1

for _, row in projects_df.iterrows():
    num_resources = random.randint(2, 5)

    for _ in range(num_resources):
        allocation = random.randint(20, 100)

        resource_id = f"RES{resource_counter:04}"

        resources.append([
            resource_id,
            row["ProjectID"],
            random.choice(roles),
            allocation,
            round(allocation * random.uniform(500, 1500), 0)
        ])

        resource_counter += 1
        
resources_df = pd.DataFrame(resources, columns=[
    "ResourceID", "ProjectID", "Role", "AllocationPct", "Cost"
])

resources_df.to_csv("data/resources.csv", index=False)

print("Portfolio dataset generated successfully.")