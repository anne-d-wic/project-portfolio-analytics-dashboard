select

    p.project_id,
    p.budget,
    p.actual_cost,
    p.budget_variance,
    p.budget_variance_pct,
    p.status,
    p.is_delayed,
    coalesce(m.total_milestones,0) as total_milestones,
    coalesce(m.delayed_milestones,0) as delayed_milestones,
    coalesce(m.avg_delay_days,0) as avg_delay_days,
    coalesce(r.total_risks,0) as total_risks,
    coalesce(r.high_risk_count,0) as high_risk_count,
    coalesce(r.avg_risk_score,0) as avg_risk_score,
    coalesce(s.total_resources,0) as total_resources,
    coalesce(s.total_allocation_pct,0) as total_allocation_pct,
    coalesce(s.total_resource_cost,0) as total_resource_cost

from {{ ref('int_projects') }} as p

left join {{ ref('int_milestones') }} as m
    on p.project_id = m.project_id
left join {{ref('int_risks')}} as r
    on p.project_id = r.project_id
left join {{ref('int_resources')}} as s
    on p.project_id = s.project_id