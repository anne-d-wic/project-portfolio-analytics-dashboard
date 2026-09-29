import duckdb
import pandas as pd
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

con = duckdb.connect(REPO_ROOT / "data" / "portfolio.duckdb")

print(con.sql("select * from main_intermediate.int_risks_detail limit 5").df())
