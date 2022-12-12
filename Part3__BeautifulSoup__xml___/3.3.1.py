from bs4 import BeautifulSoup as bs

with open('map2.osm', 'r', encoding='UTF-8') as f:
    soup = bs(f, 'xml')

res = soup.find_all('node')
fuel = 0
for i in res:
    tag = i.find('tag', v="fuel")
    if tag:
        fuel += 1

print(fuel)


# res = soup.find_all('node')
# fuel = 0
# for tag in res:
#     fuel += 1 if tag.find('tag', v="fuel") else 0
# print(fuel)


# Вася решил открыть АЗС (заправку). Чтобы оценить уровень конкуренции он хочет изучить количество заправок
# в интересующем его районе. Вася скачал интересующий его кусок карты
# OSM https://stepik.org/media/attachments/lesson/245681/map2.osm и хочет посчитать, сколько
# на нём отмечено точечных объектов (node), являющихся заправкой. В качестве ответа вам необходимо
# вывести одно число - количество АЗС.
# # "Как обозначается заправка в OpenStreetMap" - пример хорошего запроса чтобы узнать, как обозначается заправка в OpenStreetMap.