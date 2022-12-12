from bs4 import BeautifulSoup as bs
import requests
import re

html = requests.get('https://stepik.org/media/attachments/lesson/209723/5.html').text

soup = bs(html, 'html5lib')

lst2 = soup.find_all('td')
print(sum(tuple(int(s.get_text()) for s in lst2)))

print(sum(int(n) for n in re.findall('(\d+)', html)))


# В файле https://stepik.org/media/attachments/lesson/209723/5.html находится одна таблица.
# Просуммируйте все числа в ней. Теперь мы не только добавили разных тегов для изменения стиля отображения,
# но и сделали невалидный HTML-код (правда, браузеры его отображают, а вот с BeautifulSoup могут быть проблемы).
# Невалидный HTML-код - не редкость в интернете, надо учиться работать и с этим.
#
# Вы можете исправить html-код или попробовать использовать нестандартный парсер html, такой как html5lib.