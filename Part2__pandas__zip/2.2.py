import pandas as pd

data = pd.read_excel('salaries.xlsx', index_col=0)
print(data.median(axis=1).idxmax(), data.mean(axis=0).idxmax())


# Вася планирует карьеру и переезд. Для это составил таблицу, в которой для каждого региона записал зарплаты для
# разных интересные ему профессий. Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245267/salaries.xlsx.
# Выведите название региона с самой высокой медианной зарплатой (медианой называется элемент, стоящий в середине массива после
# его упорядочивания) и, через пробел, название профессии с самой высокой средней зарплатой по всем регионам.