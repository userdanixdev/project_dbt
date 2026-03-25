{% docs project_overview %}

# 🎸 Implementação de Pipeline Analítico com dbt + DuckDB (Modelagem, Snapshot e Testes)

Este projeto foi desenvolvido com o objetivo de modelar dados reais de guitarras
utilizando boas práticas de engenharia de dados com dbt.

## 🔹 Objetivo

Transformar dados brutos em um modelo analítico confiável,
permitindo análises sobre:

- preços de guitarras
- características técnicas
- histórico de alterações (snapshot)

## 🔹 Camadas do Projeto

### 🟢 Fonte (Seeds)
Dados CSV contendo informações de guitarras.

### 🔵 Dimensão (dim_guitars)
Tabela dimensional contendo atributos descritivos:
- marca
- modelo
- captadores
- país de fabricação

### 🟣 Fato (fct_guitars)
Tabela com métricas:
- preço
- chave de relacionamento com dimensão

### 🟡 Snapshot (dim_guitars_snap)
Controle de histórico com:
- dbt_valid_from
- dbt_valid_to

Permite análise temporal (SCD Type 2).

## 🔹 Tecnologias utilizadas

- dbt (data build tool)
- DuckDB
- SQL
- Snapshot (SCD Type 2)

## 🔹 Benefícios

- Versionamento de dados
- Rastreabilidade
- Estrutura analítica escalável
- Facilidade de consulta para BI

{% enddocs %}