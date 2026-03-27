![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![dbt](https://img.shields.io/badge/dbt-Analytics%20Engineering-orange?logo=dbt)
![DuckDB](https://img.shields.io/badge/DuckDB-Database-yellow?logo=duckdb)
![Git](https://img.shields.io/badge/Git-Version%20Control-red?logo=git)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-success)
![License](https://img.shields.io/badge/License-MIT-green)



#  Projeto dbt com DuckDB : Modelagem Dimensional, Snapshots (SCD Type 2) e Testes de Qualidade
## 📌 Visão Geral

Este projeto foi desenvolvido com o objetivo de aplicar conceitos de engenharia de dados utilizando **dbt (Data Build Tool)** com o banco **DuckDB**, construindo uma arquitetura analítica baseada em boas práticas de modelagem dimensional.

A solução transforma dados brutos de guitarras em um modelo estruturado, confiável e pronto para análise, com validação de qualidade e versionamento.

---

## 🎯 Objetivos do Projeto

* Estruturar dados brutos em um modelo analítico
* Aplicar boas práticas de modelagem dimensional (Star Schema)
* Implementar testes de qualidade de dados
* Utilizar snapshots para histórico de alterações (SCD Type 2)
* Criar um pipeline reprodutível com dbt

---

## 🧱 Arquitetura do Projeto

```text
Seed (dados brutos)
        ↓
Snapshot (histórico - SCD Type 2)
        ↓
Dimensão (dim_guitars)
        ↓
Fato (fct_guitars)
```

---

## 🗂️ Estrutura do Projeto:

```text
models/
  └── example/
      ├── dim_guitars.sql
      ├── fct_guitars.sql
      └── schema_guitars.yml

seeds/
  ├── guitarras.csv
  └── schema.yml

snapshots/
  └── dim_guitars_snap.sql

queries_SQL/
  ├── consulta_dim_guitars_snap.py
  ├── consulta_dim_guitars_update_snap.py
  ├── consulta_dim_guitars.py
  ├── consulta_join_dim_fact_guitars.py
  ├── consulta_view_fct_guitars.py
  ├── consulta_cars.py
  ├── consultas_guitars.py
  └── update_dim_guitars.py

```

---

## 📊 Fonte de Dados (Seed)

Os dados iniciais são carregados via `seed`, contendo informações como:

* Identificador (`id`)
* Marca
* Modelo
* País de fabricação
* Preço (`preco_usd`)
* Tipo de ponte
* Quantidade de cordas
* Configuração de captadores

---

## 🔄 Snapshot (Histórico)

Foi implementado um snapshot para manter histórico das alterações dos dados, utilizando o conceito de:

### 📌 SCD Type 2

Permite:

* Manter histórico completo de mudanças
* Identificar versões válidas de registros
* Auditoria de dados

Campos utilizados:

* `dbt_valid_from`
* `dbt_valid_to`

---

## 📐 Modelagem Dimensional

### 🔹 Dimensão: `dim_guitars`

Tabela com atributos descritivos das guitarras.

**Principais colunas:**

* `gtr_sk` → chave substituta (surrogate key)
* `gtr_sk_1` → chave natural (id original)
* `marca`
* `modelo`
* `pais_fabricacao`
* `ponte`
* `cordas`
* `captadores`

---

### 🔹 Fato: `fct_guitars`

Tabela com métricas numéricas.

**Principais colunas:**

* `guitarra_id` → chave natural
* `preco_usd` → métrica principal

---

## 🔗 Relacionamentos

* `fct_guitars.guitarra_id`
* relacionado com:
* `dim_guitars.gtr_sk_1`

---

## ✅ Testes de Qualidade (dbt Tests)

Foram implementados testes para garantir a integridade dos dados:

### 🔹 Testes aplicados:

* `not_null`
* `unique`
* `relationships`

### 📌 Exemplos:

* Garantia de unicidade da chave (`gtr_sk`)
* Verificação de integridade referencial entre fato e dimensão
* Validação de campos obrigatórios

---

## ⚙️ Tecnologias Utilizadas

* **dbt (Data Build Tool)**
* **DuckDB**
* **SQL**
* **Python (para consultas e validações externas)**
* **VSCode**

---

## 🚀 Execução do Projeto

### 🔹 Rodar models

```bash
dbt run
```

### 🔹 Executar testes

```bash
dbt test
```

### 🔹 Carregar seeds

```bash
dbt seed
```

### 🔹 Executar snapshots

```bash
dbt snapshot
```
### 🔹 Gerar documentação
```bash
dbt docs generate
```

### 🔹 Subir servidor local (localhost)
```bash
dbt docs serve
```

### 🌐 Acessar no navegador:
```
Após executar o comando acima, abrirá automaticamente:

http://localhost:8080
```
---

### 📊 Scripts de Consulta e Validação (DuckDB)

Os scripts abaixo são utilizados para validar, consultar e testar os dados gerados pelo dbt diretamente no banco DuckDB, garantindo a integridade das transformações e do modelo dimensional.

## 🔎 Descrição dos Arquivos:

```consulta_dim_guitars.py```
- Consulta direta da dimensão ```dim_guitars```, permitindo validar os dados transformados pelo dbt.

`Consulta_dim_guitars_snap.py`
- Consulta a tabela de snapshot `dim_guitars_snap`, exibindo o histórico de alterações (SCD Type 2).

`consulta_dim_guitars_update_snap.py`

- Utilizado para validar atualizações no snapshot após mudanças nos dados de origem.

`consulta_join_dim_fact_guitars.py`

- Realiza o JOIN entre a dimensão`(dim_guitars_snap)` e a tabela fato, simulando uma consulta analítica.

`consulta_view_fct_guitars.py`

- Consulta a view da tabela fato (fct_guitars), utilizada para análises de métricas.

`consulta_cars.py`

- Script auxiliar para consulta de dados de exemplo relacionados a carros (base inicial do projeto).

`consultas_guitars.py`

- Script consolidado com múltiplas consultas analíticas para exploração dos dados de guitarras.

`update_dim_guitars.py`

- Executa atualizações nos dados da dimensão, permitindo testar o comportamento do snapshot (SCD Type 2).


Esses scripts funcionam como uma camada de validação e exploração, permitindo:

- Conferir se os modelos dbt foram criados corretamente
- Validar o comportamento do snapshot (histórico de dados)
- Simular consultas analíticas (JOIN fato + dimensão)
- Testar alterações nos dados e seu impacto no modelo

## 📈 Benefícios da Solução

* Dados organizados e padronizados
* Pipeline reprodutível
* Facilidade para análises futuras
* Garantia de qualidade com testes automatizados
* Histórico completo das alterações

---

## 🔮 Possíveis Evoluções

* Integração com ferramentas de BI (Power BI, Metabase, Looker)
* Criação de dashboards analíticos
* Implementação de camadas (staging, intermediate, mart)
* Orquestração com Airflow ou similar
* Deploy em ambiente cloud

---

## 👨‍💻 Autor

*Projeto desenvolvido por **Daniel M.F.** com foco em aprendizado e aplicação prática de engenharia de dados moderna.*


🔗 Conecte-se comigo no LinkedIn:  

👉 https://www.linkedin.com/in/danixdev