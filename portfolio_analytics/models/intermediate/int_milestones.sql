select 
	project_id,
	count(*) as total_milestones,
	avg(delay_days) as avg_delay_days,
	sum(case when delay_days > 0 then 1 else 0 end) as delayed_milestones
from {{ref('stg_milestones')}}
group by project_id