with detail_counts as (
    select
        project_id,
        sum(case when risk_level = 'High' then 1 else 0 end) as high_risk_count
    from {{ ref('int_risks_detail') }}
    group by project_id
)

select
    fps.project_id,
    fps.high_risk_count,
    coalesce(dc.high_risk_count, 0) as detail_high_risk_count
from {{ ref('fct_project_summary') }} as fps
left join detail_counts as dc
    on fps.project_id = dc.project_id
where fps.high_risk_count != coalesce(dc.high_risk_count, 0)
