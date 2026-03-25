import duckdb
from pathlib import Path

db_path = Path(__file__).resolve().parents[1] / "model_test" / "seeds" / "dev_guitarras.duckdb"
con = duckdb.connect(str(db_path))

con.execute("""
    update main.guitarras
    set
        ponte = 'Floyd Rose',
        captadores = 'HSH',
        preco_usd = 1599.99
    where id = 1
""")

print("Update realizado com sucesso.")