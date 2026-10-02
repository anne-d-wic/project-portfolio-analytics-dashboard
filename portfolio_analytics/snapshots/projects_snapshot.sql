{% snapshot projects_snapshot %}

{{
    config(
        target_schema='snapshots',
        unique_key='project_id',
        strategy='check',
        check_cols=['status', 'priority', 'actual_cost', 'end_date']
    )
}}

select
    project_id,
    status,
    priority,
    actual_cost,
    end_date
from {{ ref('stg_projects') }}

{% endsnapshot %}