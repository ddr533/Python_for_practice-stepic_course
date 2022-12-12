from bs4 import BeautifulSoup as bs
import requests

html = requests.get('https://stepik.org/media/attachments/lesson/209723/4.html').text

soup = bs(html, 'html.parser')
lst = soup.find_all('td')
print(sum(tuple(int(s.get_text()) for s in lst)))

# В файле https://stepik.org/media/attachments/lesson/209723/4.html находится одна таблица.
# Просуммируйте все числа в ней. Теперь мы добавили разных тегов для изменения стиля отображения.
# Для доступа к ячейкам используйте возможности BeautifulSoup.