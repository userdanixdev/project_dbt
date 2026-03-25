import duckdb
from pathlib import Path
import pandas as pd

db_path = Path(__file__).resolve().parents[1] / "model_test" / "seeds" / "dev_guitarras.duckdb"
con = duckdb.connect(str(db_path))

df = con.execute("""
    SELECT *
    FROM main.dim_guitars_snap
    ORDER BY gtr_sk_1, dbt_valid_from
""").fetchdf()

print(df)