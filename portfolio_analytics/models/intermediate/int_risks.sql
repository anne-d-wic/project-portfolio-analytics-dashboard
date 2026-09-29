select 
	project_id,
	count(*) as total_risks,
	sum(case when risk_level = 'High' then 1 else 0 end) as high_risk_count,
	avg(impact * probability) as avg_risk_score
from {{ref('stg_risks')}}
group by project_id