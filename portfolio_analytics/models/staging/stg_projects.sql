select 
	"ProjectID" as project_id,
	"ProjectName" as project_name,
	"Program" as program,
	cast("StartDate" as date) as start_date,
	cast("EndDate" as date) as end_date,
	"Budget" as budget,
	"ActualCost" as actual_cost,
	"Status" as status,
	"Priority" as priority,
	"Sponsor" as sponsor
from {{ref('projects')}}