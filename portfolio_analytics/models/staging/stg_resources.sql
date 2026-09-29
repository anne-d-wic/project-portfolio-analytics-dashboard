select 
	"ResourceID" as resource_id,
	"ProjectID" as project_id,
	"Role" as role,
	"AllocationPct" as allocation_pct,
	"Cost" as cost
from {{ref('resources')}}