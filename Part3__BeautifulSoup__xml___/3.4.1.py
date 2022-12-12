from bs4 import BeautifulSoup as bs

with open('map2.osm', 'r', encoding='UTF-8') as f:
    soup = bs(f, 'xml')

res = soup.find_all(k="amenity", v="fuel")


print(len(res))


# Вася, открывший заправку в прошлом уроке, разорился. Конкуренция оказалась слишком большой.
# Вася предполагает, что это произошло от того, что теги заправки могут быть не только на точке, но и на каком-то контуре.
# Определите, сколько заправок на самом деле (не только обозначенных точкой) есть на фрагменте карты
# https://stepik.org/media/attachments/lesson/245681/map2.osm