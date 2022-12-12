import pandas as pd

data1 = pd.read_excel(r'C:\Users\AndreyPC\PycharmProjects\Python_practic\Part2__xlsx___\trekking3.xlsx', sheet_name=0).fillna(0)
data2 = pd.read_excel(r'C:\Users\AndreyPC\PycharmProjects\Python_practic\Part2__xlsx___\trekking3.xlsx', sheet_name=1).fillna(0)
data3 = data2.merge(data1, left_on='Продукт', right_on='Unnamed: 0', how='inner').sort_values('День')
data3 = data3.drop(columns=['Unnamed: 0'])
data4 = data3.apply(lambda x: pd.concat([x[:2], (x[3:]*x[2]/100)]), axis=1)
data5 = data4.groupby('День').sum().astype('int')
print(*data5.values)

# Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно,
# составив справочник продуктов с указанием калорийности на 100 грамм, а также содержание белков, жиров и
# углеводов на 100 грамм продукта. Ему не удалось найти всю информацию, поэтому некоторые ячейки остались незаполненными
# (можно считать их значение равным нулю). Также он использовал какой-то странный офисный пакет и разделял
# целую и дробную часть чисел запятой. Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking3.xlsx
#
# Вася составил раскладку по продуктам на весь поход (она на листе "Раскладка") с указанием номера дня, названия
# продукта и его количества в граммах. Для каждого дня посчитайте 4 числа: суммарную калорийность и
# граммы белков, жиров и углеводов. Числа округлите до целых вниз и введите через пробел. Информация о каждом дне
# должна выводиться в отдельной строке.

