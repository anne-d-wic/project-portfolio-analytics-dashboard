select 
	project_id,
	project_name,
	program,
	priority,
	sponsor
from {{ref('int_projects')}}