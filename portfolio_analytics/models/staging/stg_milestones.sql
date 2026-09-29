select 
	"MilestoneID" as milestone_id,
	"ProjectID" as project_id,
	"MilestoneName" as milestone_name,
	cast("PlannedDate" as date) as planned_date,
	cast("ActualDate" as date) as actual_date,
	"DelayDays" as delay_days
from {{ref('milestones')}}