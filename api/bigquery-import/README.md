# Імпорт CSV у BigQuery

Ноутбук `ImportBQ.ipynb` завантажує `import_BQ.csv` (колонки `Query` і `Frequency`) у таблицю BigQuery. Далі з цими даними зручно працювати в SQL або Looker Studio.

## Налаштування

1. У Google Cloud створіть сервісний акаунт з роллю BigQuery Data Editor і збережіть JSON-ключ поруч з ноутбуком як `service_account.json`.
2. У виклику `to_gbq` вкажіть:
   - `project_id` - ID вашого проєкту в Google Cloud;
   - `destination_table` - датасет і таблицю у форматі `датасет.таблиця`.
3. Якщо у вашому CSV інші колонки, поправте `schema`.

`if_exists='replace'` перезаписує таблицю. Щоб дописувати рядки, змініть на `'append'`.

```bash
pip install pandas pandas-gbq google-auth
```
