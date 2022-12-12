from bs4 import BeautifulSoup as bs

with open('map1.osm', 'r', encoding='UTF-8') as f:
    soup = bs(f, 'xml')

node = 0
node_tag = 0

for elem in soup.find_all('node'):
    if elem.find('tag'):
        node_tag += 1
    else:
        node += 1

print(node_tag, node)


# В OpenStreetMap XML встречаются теги node, которые соответствуют некоторым точкам на карте.
# Ноды могут не только обозначать какой-то точечный объект, но и входить в состав way (некоторой линии, возможно замкнутой)
# и не иметь собственных тегов. Для доступного по ссылке https://stepik.org/media/attachments/lesson/245678/map1.osm
# фрагмента карты посчитайте, сколько node имеет хотя бы один вложенный тэг tag, а сколько - не имеют.
# В качестве ответа введите два числа, разделённых пробелом.