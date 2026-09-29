select 
	"RiskID" as risk_id,
	"ProjectID" as project_id,
	"RiskLevel" as risk_level,
	"Impact" as impact,
	"Probability" as probability,
	"Status" as status
from {{ref('risks')}}