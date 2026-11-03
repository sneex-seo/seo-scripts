# Канібалізація запитів у Google Search Console

Ноутбук `cannibalization.ipynb` вивантажує з GSC пари «сторінка + запит» за період і знаходить запити, за якими ранжуються дві й більше сторінок сайту.

## Як працює

1. Авторизація через OAuth: відкриється браузер, де треба увійти в Google-акаунт з доступом до GSC.
2. `account.webproperties` показує список сайтів у консолі, далі обираєте потрібний: `account['https://example.com/']`.
3. Задаєте період у `query.range(start=..., stop=...)`.
4. Фільтр: залишаються рядки від 5 показів. За потреби можна відсіяти брендові запити та службові сторінки, для цього розкоментуйте блок зі стоп-словами.
5. Результат: `cannibalization.xlsx` з колонками запит, сторінка, кліки, покази, CTR, позиція.

## Налаштування

1. У Google Cloud створіть OAuth-клієнт типу «Desktop app» і завантажте JSON.
2. Збережіть його поруч з ноутбуком як `credentials_for_GSC.json`.
3. Встановіть бібліотеки:

```bash
pip install pandas openpyxl pydata-google-auth google-api-python-client git+https://github.com/joshcarty/google-searchconsole
```
