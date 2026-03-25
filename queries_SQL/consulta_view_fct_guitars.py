import duckdb
from pathlib import Path

db_path = Path(__file__).resolve().parents[1] / "model_test" / "seeds" / "dev_guitarras.duckdb"
con = duckdb.connect(str(db_path))

df = con.execute("SELECT * FROM main.fct_guitars").fetchdf()

print(df)