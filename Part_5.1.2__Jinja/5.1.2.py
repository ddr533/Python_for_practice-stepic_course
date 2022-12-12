html_page = '<html>\n<body>\n<table>'

for tr in range(1, 11):
    html_page = html_page + '<tr>'
    for v in range(tr, tr * 10 + tr, tr):
        html_page = html_page + f'<td><a href=http://{v}.ru>{v}</a></td>'
    html_page = html_page + '</tr>' + '\n'

html_page = html_page + '</table>\n</body>\n</html>'

with open('html_res.html', 'w', encoding='UTF-8') as f:
    f.write(html_page)



# from jinja2 import Template
# template = Template("""      <tr>           {% for item in my_array %}
#            <td><a href="http://{{item}}.ru">{{item}}</a></td>     {% endfor %}
#       </tr> """)
# print('<html>', '<body>', '  <table>', sep='\n  ')
# for i in range(1, 11):  print(template.render(my_array=range(i, i*11, i)))
# print('    </table>', '  </body>', '</html>', sep='\n')




# from jinja2 import Template
# template = Template('''<html>
#     <body>#         <table>
#             {% for i in nums %}<tr>
#                 {% for j in nums %}<td>{{i*j}}</td>
#                 {% endfor %}
#             </tr>
#             {% endfor %}
#         </table>
#     </body>
# </html>''')
#
# nums = [i for i in range(1,11)]
#
# with open('table.html', 'w') as html:
#     html.write(template.render(nums=nums))