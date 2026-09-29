import duckdb
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

con = duckdb.connect('data/portfolio.duckdb')

print(con.sql("select * from main_intermediate.int_risks_detail limit 5").df())
