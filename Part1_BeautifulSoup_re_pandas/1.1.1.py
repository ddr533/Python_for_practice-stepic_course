import requests

html = requests.get('https://stepik.org/media/attachments/lesson/209717/1.html').text
print('Python' if html.count('Python') > html.count('C++') else 'C++')


# Мы сохранили страницу с википедии про языки программирования и сохранили по адресу https://stepik.org/media/attachments/lesson/209717/1.html
#
# Скачайте её с помощью скрипта на Питоне и посчитайте, какой язык упоминается чаще Python или C++ (ответ должен быть одной из этих двух строк).