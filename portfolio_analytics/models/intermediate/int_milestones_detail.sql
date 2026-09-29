select 
	milestone_id,
    project_id,
    milestone_name,
    planned_date,
    actual_date,
    delay_days,
	case when delay_days > 0 then 1 else 0 end as is_delayed_milestone
from {{ref('stg_milestones')}}