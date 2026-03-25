select
    {{ generate_key_hash([
        'marca',
        'modelo',
        'pais_fabricacao'
    ]) }} as gtr_sk,

    id as gtr_sk,
    marca,
    modelo,
    pais_fabricacao,
    ponte,
    cordas,
    captadores

from {{ ref('guitarras') }}