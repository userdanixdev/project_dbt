import duckdb
from pathlib import Path
import pandas 

db_path = Path(__file__).resolve().parents[1] / "model_test" / "dev.duckdb"

con = duckdb.connect(str(db_path))

df = con.execute("SELECT * FROM carros").fetchdf()

print(df)