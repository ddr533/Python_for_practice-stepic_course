import pandas as pd
import zipfile

res_list = []

with zipfile.ZipFile('rogaikopyta.zip') as myzip:
    for name in myzip.namelist():
        with myzip.open(name) as myfile:
            data = pd.read_excel(myfile).iloc[[0],[1,3]].values
            res_data = [data[0][0], str(int(data[0][1]))]
        res_list.append(res_data)

res_list = sorted(res_list, key=lambda x: x[0])

with open('res2.txt','w', encoding='UTF-8') as res_data:
    for d in res_list:
        res_data.write(' '.join(d))
        res_data.write('\n')


# Главный бухгалтер компании "Рога и копыта" случайно удалил ведомость с начисленной зарплатой. К счастью,
# у него сохранились расчётные листки всех сотрудников.
# Помогите по этим расчётным листкам восстановить зарплатную ведомость. Архив с расчётными листками доступен
# по ссылке https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip
# (вы можете скачать и распаковать его вручную или самостоятельно научиться делать это с помощью скрипта на Питоне).
#
# Ведомость должна содержать 1000 строк, в каждой строке должно быть указано ФИО сотрудника и, через пробел, его зарплата.
# Сотрудники должны быть упорядочены по алфавиту.