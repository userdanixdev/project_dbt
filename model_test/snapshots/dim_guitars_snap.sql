{% snapshot dim_guitars_snap %}

{{
    config(
        target_schema='main',
        unique_key='gtr_sk_1',
        strategy='check',
        check_cols=[
            'marca',
            'modelo',
            'pais_fabricacao',
            'ponte',
            'cordas',
            'captadores'
        ]
    )
}}

select
    gtr_sk,
    gtr_sk_1,
    marca,
    modelo,
    pais_fabricacao,
    ponte,
    cordas,
    captadores
from {{ ref('dim_guitars') }}

{% endsnapshot %}