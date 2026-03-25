
import duckdb
from pathlib import Path
import pandas 

db_path = Path(__file__).resolve().parents[1] / "model_test" / "seeds" / "dev_guitarras.duckdb"
con = duckdb.connect(str(db_path))

df = con.execute("""
    select
        d.gtr_sk,
        g.id as guitarra_id,
        g.preco_usd,
        d.marca,
        d.modelo,
        d.dbt_valid_from,
        d.dbt_valid_to
    from main.guitarras g
    inner join main.dim_guitars_snap d
        on g.id = d.gtr_sk_1
    order by g.id, d.dbt_valid_from
""").fetchdf()

print(df)


## Se usar o filtro: 'where d.dbt_valid_to is null', Você só verá registros atuais, então:
## dbt_valid_from → preenchido // dbt_valid_to → sempre NULL

