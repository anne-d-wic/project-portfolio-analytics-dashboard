select 
	project_id,
	count(*) as total_resources,
	sum(allocation_pct) as total_allocation_pct,
	sum(cost) as total_resource_cost
from {{ref('stg_resources')}}
group by project_id