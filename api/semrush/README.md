# Semrush API

Три скрипти для роботи з [Semrush API](https://developer.semrush.com/api/). Наприкінці кожен виводить залишок API-юнітів на балансі.

| Скрипт | Звіт Semrush | Вхід | Вихід |
|---|---|---|---|
| `domainorganic.py` | `phrase_this`: частотність, CPC, конкуренція, кількість результатів і тренд для кожного запиту | `domains.txt`, по одному запиту в рядку | `winnerloser.csv` |
| `domainranks.py` | `domain_ranks`: кількість органічних ключів, трафік і його вартість для кожного домену | `domainranks.txt`, по одному домену в рядку | `domainranks.csv` |
| `winnerlosers.py` | `rank_difference`: домени, які найбільше виросли або просіли в органіці | - | `winnerloser.csv` |

## Налаштування

API-ключ передається через змінну оточення `SEMRUSH_API_KEY`:

```bash
pip install requests-html
export SEMRUSH_API_KEY="ваш_ключ"
python domainranks.py
```

У Windows PowerShell замість `export`: `$env:SEMRUSH_API_KEY="ваш_ключ"`.

База регіону задається змінною `region` у коді (зараз `ua`), а кількість рядків у `winnerlosers.py` - змінною `limit`.

API Semrush платний: кожен рядок відповіді списує юніти. Звіт `rank_difference` на 10 000 рядків коштує близько 200 тис. юнітів, тому починайте з малого `limit`.
