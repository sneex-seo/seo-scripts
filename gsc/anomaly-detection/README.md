# Аномалії в даних Google Search Console

Ноутбук `anomaly_detection.ipynb` вивантажує щоденні покази, кліки та CTR сайту з GSC і позначає на графіках дні з аномальними сплесками й просіданнями.

## Як працює

- Дані беруться через Search Console API (`webmasters v3`) з розбивкою по датах.
- Для пошуку аномалій використовується `PersistAD` з бібліотеки [ADTK](https://adtk.readthedocs.io/): окремо для зростання (`positive`), падіння (`negative`) та обох напрямків (`both`).
- Сайт і період задаються в комірці з `payload` та `site_url`.

## Налаштування

1. У Google Cloud створіть сервісний акаунт, увімкніть Search Console API і завантажте JSON-ключ.
2. Збережіть ключ поруч з ноутбуком як `client_secrets.json`.
3. У Google Search Console додайте email сервісного акаунта користувачем ресурсу.
4. Встановіть бібліотеки:

```bash
pip install pandas google-auth google-api-python-client adtk
```
