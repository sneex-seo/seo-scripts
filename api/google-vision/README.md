# Хто використовує ваші зображення

Скрипт перевіряє кожне зображення через Google Vision API (Web Detection) і знаходить сторінки інших сайтів, де воно трапляється. Так можна знайти, хто скопіював фото, і попросити посилання на джерело.

- `googlevisio.py` - для `google-cloud-vision` до версії 2.0.
- `googlevisio_v2.py` - для `google-cloud-vision` 2.0 і новіших.

## Як запустити

1. У Google Cloud увімкніть [Cloud Vision API](https://cloud.google.com/vision), створіть сервісний акаунт і збережіть JSON-ключ поруч зі скриптом як `credentials.json`.
2. Впишіть прямі посилання на зображення у `linksfile.txt`, по одному в рядку.
3. У коді вкажіть свій домен у `checked_site`, щоб власні сторінки не потрапили в результат.
4. Запустіть:

```bash
pip install google-cloud-vision
python googlevisio_v2.py
```

Результат дописується в `imagessteal.csv`: посилання на зображення та сторінка, де його знайдено.
