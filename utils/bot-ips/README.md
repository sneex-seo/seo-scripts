# IP-адреси Googlebot і Bingbot

`google_and_bing_ips.py` завантажує офіційні списки діапазонів IP [Googlebot](https://developers.google.com/search/apis/ipranges/googlebot.json) і [Bingbot](https://www.bing.com/toolbox/bingbot.json) та розгортає їх у перелік окремих IPv4-адрес.

Навіщо: в аналізі логів сервера можна відрізнити справжніх ботів від тих, хто лише підставляє їхній User-Agent.

```bash
pip install pandas requests
python google_and_bing_ips.py
```

Результат: `Bot_ips.csv` з колонками `bot_name` і `ip_address`. IPv6-діапазони скрипт пропускає.
