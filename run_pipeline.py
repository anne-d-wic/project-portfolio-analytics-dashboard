import subprocess
import sys
from datetime import datetime

import os
os.makedirs("logs", exist_ok=True)

def log(message):
    line = f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {message}"
    print(line)
    with open("logs/pipeline.log", "a", encoding="utf-8") as f:
        f.write(line + "\n")

# Call dbt through the running interpreter so the pipeline uses the active venv,
# not whatever "dbt" happens to be on the system PATH.
DBT = [sys.executable, "-m", "dbt.cli.main"]

steps = [
    ["seed"],
    ["run"],
    ["test"],
]

for step in steps:
    log(f"Starting: dbt {' '.join(step)}")
    result = subprocess.run(DBT + step, cwd="portfolio_analytics")
    if result.returncode != 0:
        log(f"Failed: dbt {' '.join(step)}")
        sys.exit(result.returncode)
    else:
        log(f"Succeeded: dbt {' '.join(step)}")

log("All steps succeeded.")