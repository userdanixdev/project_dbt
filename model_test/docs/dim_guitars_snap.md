{% docs dim_guitars_snap %}

## 🎸 Dimensão de 'Guitars' (Snapshot)

A tabela **dim_guitars_snap** é uma dimensão histórica construída utilizando a funcionalidade de **snapshots do dbt**. Seu principal objetivo é armazenar a evolução dos atributos das guitarras ao longo do tempo, permitindo análises temporais e auditoria de mudanças.

---

## 📌 Objetivo

Registrar alterações nos dados das guitarras (como marca, modelo, país de fabricação, ponte, número de cordas e captadores), garantindo histórico completo através de controle de validade.

---

## 🧱 Estrutura da Tabela

| Coluna            | Descrição |
|------------------|----------|
| `gtr_sk`         | Chave substituta (surrogate key) da guitarra |
| `gtr_sk_1`       | Chave original da tabela fonte (`guitarras.id`) |
| `marca`          | Marca da guitarra |
| `modelo`         | Modelo da guitarra |
| `pais_fabricacao`| País onde a guitarra foi fabricada |
| `ponte`          | Tipo de ponte |
| `cordas`         | Quantidade de cordas |
| `captadores`     | Tipo de captadores |
| `dbt_valid_from` | Timestamp de início da validade do registro |
| `dbt_valid_to`   | Timestamp de fim da validade (NULL = registro atual) |

---

## ⏳ Controle de Histórico (SCD Tipo 2)

A tabela segue o padrão **Slowly Changing Dimension Type 2 (SCD2)**:

- Cada alteração nos dados gera um novo registro
- O registro antigo recebe um `dbt_valid_to`
- O registro atual mantém `dbt_valid_to = NULL`

---

## 🔄 Exemplo de Uso

Consulta para obter apenas os registros atuais:

```
SELECT *
FROM dim_guitars_snap
WHERE dbt_valid_to IS NULL
```

{% enddocs %}