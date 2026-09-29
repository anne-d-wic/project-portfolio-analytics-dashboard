select 
	risk_id,
    project_id,
    risk_level,
    impact,
    probability,
    status,
	case when risk_level = 'High' then 1 else 0 end as is_high_risk,
	impact * probability as risk_score
from {{ref('stg_risks')}}