import duckdb
from pathlib import Path

db_path = Path(__file__).resolve().parents[1] / "model_test" / "seeds" / "dev_guitarras.duckdb"
con = duckdb.connect(str(db_path))

df = con.execute("""
    select
        gtr_sk,
        gtr_sk_1,
        marca,
        modelo,
        ponte,
        captadores,
        dbt_valid_from,
        dbt_valid_to
    from main.dim_guitars_snap
    where gtr_sk_1 = 1
    order by dbt_valid_from
""").fetchdf()

print(df)

# Obs: Antes do update, a guitarra 1 tinha ponte = Tremolo e captadores = SSS.
# Depois do update e do dbt snapshot, você deve ver duas linhas para gtr_sk_1 = 1:
# uma linha antiga com dbt_valid_to preenchido e uma linha nova com dbt_valid_to = NULL

# Fluxo certo:
## UPDATE main.guitarras ... // dbt snapshot -s dim_guitars_snap // consultar main.dim_guitars_snap

