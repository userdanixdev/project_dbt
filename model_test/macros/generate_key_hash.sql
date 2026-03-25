{% macro generate_key_hash(columns) %}

md5(
    concat(
        {% for col in columns %}
            coalesce(cast({{ col }} as varchar), '')
            {% if not loop.last %}, '|' ,{% endif %}
        {% endfor %}
    )
)

{% endmacro %}

-- junta as colunas, trata NULL, gera hash MD5 e cria chave única consistente --

