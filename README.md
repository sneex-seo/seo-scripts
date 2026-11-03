# seo-scripts

Python-скрипти для SEO, які я писав для роботи та для Telegram-каналу [@seo_scripts](https://t.me/seo_scripts) у 2021-2024 роках. Раніше кожен лежав в окремому репозиторії, тепер вони зібрані тут.

Свіжіший і більший інструмент - [seo-analyzer](https://github.com/sneex-seo/seo-analyzer): діагностика, чому сторінка нижча за конкурентів у Google.

## Що всередині

| Папка | Що робить | Було в репозиторії |
|---|---|---|
| [gsc/cannibalization](gsc/cannibalization) | Шукає канібалізацію: запити, за якими в Google Search Console ранжуються кілька сторінок | [GSC-extractor](https://github.com/sneex-seo/GSC-extractor) |
| [gsc/anomaly-detection](gsc/anomaly-detection) | Знаходить аномальні сплески й просідання показів, кліків і CTR у GSC | [google-search-console-anomaly-detection](https://github.com/sneex-seo/google-search-console-anomaly-detection) |
| [keywords/google-suggest](keywords/google-suggest) | Збирає підказки Google за списком ключів і чистить їх стоп-словами | [suggest_google](https://github.com/sneex-seo/suggest_google) |
| [keywords/keyword-extraction](keywords/keyword-extraction) | Витягує головні ключові слова з тексту (YAKE) | [tfidf](https://github.com/sneex-seo/tfidf) |
| [keywords/clustering](keywords/clustering) | Базова кластеризація ключів: TF-IDF + Affinity Propagation | [basic_clusterization_tool](https://github.com/sneex-seo/basic_clusterization_tool) |
| [api/semrush](api/semrush) | Метрики ключів і доменів та звіт «переможці й переможені» через Semrush API | [sermrush_api](https://github.com/sneex-seo/sermrush_api) |
| [api/google-translate](api/google-translate) | Масовий переклад ключів або тексту через Google Cloud Translation | [google_translation_api](https://github.com/sneex-seo/google_translation_api) |
| [api/google-vision](api/google-vision) | Шукає сайти, які використовують ваші зображення (Google Vision, Web Detection) | [google_vision_api_seo](https://github.com/sneex-seo/google_vision_api_seo) |
| [api/bigquery-import](api/bigquery-import) | Завантажує CSV з ключами в таблицю BigQuery | [import_big_query](https://github.com/sneex-seo/import_big_query) |
| [utils/split-csv](utils/split-csv) | Ріже великий CSV на частини заданого розміру | [how_divide_or_cut_csv_file](https://github.com/sneex-seo/how_divide_or_cut_csv_file) |
| [utils/bot-ips](utils/bot-ips) | Вивантажує всі IP Googlebot і Bingbot в CSV для аналізу логів | [Google_and_Bing_bot_IPs](https://github.com/sneex-seo/Google_and_Bing_bot_IPs) |
| [utils/subdomains](utils/subdomains) | Перебирає піддомени за словником і зберігає знайдені разом з IP | [parsing_subdomains_seo](https://github.com/sneex-seo/parsing_subdomains_seo) |

Telegram-бот для Google Indexing API живе окремо: [indexing_bot_GSC](https://github.com/sneex-seo/indexing_bot_GSC).

## Як запускати

1. Потрібен Python 3 і бібліотеки, перелічені в README потрібної папки.
2. Скрипти читають вхідні файли зі своєї папки, тож запускайте їх звідти:

   ```bash
   cd keywords/google-suggest
   python suggest.py
   ```

3. Ноутбуки (`.ipynb`) відкривайте в Jupyter або VS Code.

## Ключі та доступи

- API-ключ Semrush передається через змінну оточення `SEMRUSH_API_KEY`.
- Для Google API потрібен JSON-файл сервісного акаунта або OAuth-клієнта. Назва файлу вказана в README папки.
- Файли з ключами та `.env` додані в `.gitignore`. Не комітьте їх.

## Важливо

Скрипти перенесені майже без змін: я лише виніс ключі з коду, прибрав дані клієнтів із ноутбуків і виправив синтаксичну помилку в `split-csv`. Частина коду написана під бібліотеки 2021 року, тому на свіжих версіях може знадобитися доопрацювання. Де це відомо, про це сказано в README папки.

## Ліцензія

[MIT](LICENSE)
