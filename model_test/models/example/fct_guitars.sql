select
    id as guitarra_id,
    preco_usd
from {{ ref('guitarras') }}

