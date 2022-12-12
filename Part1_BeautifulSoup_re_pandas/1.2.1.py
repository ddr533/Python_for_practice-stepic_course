import requests
import re
import pandas as pd
import collections
import bs4

html = requests.get('https://stepik.org/media/attachments/lesson/209719/2.html').text

soup = bs4.BeautifulSoup(html, 'html.parser')
lst = [x.get_text() for x in soup.find_all('code')]
print(collections.Counter(lst))

# pattern = r'<code>(.*?)<\/code>'
# res = re.findall(pattern, html)
# res_count = sorted(set((i, res.count(i)) for i in res), key=lambda x: x[1], reverse=True)
# # print(' '.join(sorted(i[0] for i in filter(lambda x: x[1] == res_count[0][1], res_count))))
# l = sorted(i[0] for i in filter(lambda x: x[1] == res_count[0][1], res_count))
# for i in l:
#     print(i, end=' ')



# df = pd.DataFrame(res)
# res_count2 = df.value_counts().head(3).index.sort_values().tolist()
# print(res_count2)
# print(' '.join(res_count2))


# C = collections.Counter(res)
# print(*(key for key in C.keys()))




# Файл https://stepik.org/media/attachments/lesson/209719/2.html содержит статью с Википедии про язык Python.
# В этой статье есть теги code, которыми выделяются конструкции на языке Python. Вам нужно найти все строки,
# содержащиеся между тегами <code> и </code> и найти те строки, которые встречаются чаще всего и вывести их
# в алфавитном порядке, разделяя пробелами.
#
# Например, если исходный текст страницы выглядел бы так:
#
# <code>a</code>
# <a>bracadabr</a>
# <code>c</code>
# <code>b</code>
# <code>b</code>
# <code>c</code>
# то в ответ надо было бы ввести строку "b c".
