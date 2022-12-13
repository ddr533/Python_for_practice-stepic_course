#!/usr/bin/env python3
import cgi
import html
import pandas as pd
from jinja2 import Template, Environment, FileSystemLoader

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "не задано")
text1 = html.escape(text1)


data = pd.read_csv(r'C:\Users\AndreyPC\PycharmProjects\Python_practic\Part5__form__with__parce\cgi-bin\data.tsv',
                   sep='\t', header=None, encoding='UTF-8')
data = data.apply(lambda x: x.str.strip(), axis=0)
data.index = data[0]
data = data.drop(columns=[0,1,3,4,5,6,7])

file_loader = FileSystemLoader(r'C:\Users\AndreyPC\PycharmProjects\Python_practic\Part5__form__with__parce\cgi-bin\templates')
env = Environment(loader=file_loader)
tm = env.get_template('res.html')
res = tm.render(data_res = data.loc['Russia'][2], text1=text1)
print("Content-type: text/html\n")
print(res)






# print("Content-type: text/html\n")
# print("""<!DOCTYPE HTML>
#         <html>
#         <head>
#             <meta charset="utf-8">
#             <title>Обработка данных форм</title>
#         </head>
#         <body>""")
#
# print("<h1>Обработка данных форм!</h1>")
# print(f"<p>TEXT_1: {text1}</p>")
#
# print("""</body>
#         </html>""")