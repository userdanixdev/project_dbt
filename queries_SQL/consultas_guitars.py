import duckdb
from pathlib import Path
import pandas 

db_path = Path(__file__).resolve().parents[1] / "model_test" / "seeds" / "dev_guitarras.duckdb"

con = duckdb.connect(str(db_path))

df = con.execute("SELECT * FROM guitarras LIMIT 10").fetchdf()

print(df)