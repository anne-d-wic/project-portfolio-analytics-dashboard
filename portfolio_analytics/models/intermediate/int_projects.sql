select 
	project_id,
	project_name,
	program,
	start_date,
	end_date,
	budget,
	actual_cost,
	status,
	priority,
	sponsor,
	actual_cost - budget as budget_variance,
	(actual_cost - budget) / budget as budget_variance_pct,
	date_diff('day', start_date, end_date) as project_duration_days,
	case when status = 'Delayed' then 1 else 0 end as is_delayed
from {{ref('stg_projects')}}