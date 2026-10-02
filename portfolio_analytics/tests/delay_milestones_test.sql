with detail_counts as (
    select
        project_id,
        sum(case when delay_days > 0 then 1 else 0 end) as delayed_milestones
    from {{ ref('int_milestones_detail') }}
    group by project_id
)

select
    fps.project_id,
    fps.delayed_milestones,
    coalesce(dc.delayed_milestones, 0) as detail_delayed_milestones
from {{ ref('fct_project_summary') }} as fps
left join detail_counts as dc
    on fps.project_id = dc.project_id
where fps.delayed_milestones != coalesce(dc.delayed_milestones, 0)
