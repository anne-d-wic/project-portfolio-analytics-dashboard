select
    milestone_id,
    planned_date,
    actual_date,
    delay_days
from {{ ref('stg_milestones') }}
where delay_days != date_diff('day', planned_date, actual_date)