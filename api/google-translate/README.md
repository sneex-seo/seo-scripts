# Масовий переклад через Google Cloud Translation

`googletranslate.py` перекладає список ключів або рядків тексту на потрібну мову. Корисно, коли треба швидко перенести семантику на інший ринок.

## Як запустити

1. У Google Cloud увімкніть [Cloud Translation API](https://console.cloud.google.com/marketplace/product/google/translate.googleapis.com).
2. Створіть сервісний акаунт, завантажте JSON-ключ і вкажіть шлях до нього в рядку `GOOGLE_APPLICATION_CREDENTIALS` (зараз `yourfilecredentials.json`).
3. Впишіть текст у `translate.txt`, по одному фрагменту в рядку.
4. Мова перекладу задається в `target = 'en'`. Коди мов є в [документації](https://cloud.google.com/translate/docs/languages).
5. Запустіть:

```bash
pip install "google-cloud-translate<2.0"
python googletranslate.py
```

Переклад дописується в `translate_en.txt`.

Скрипт написаний під `google-cloud-translate` 1.x. На версії 2.0+ замініть імпорт на `from google.cloud import translate_v2 as translate`.
