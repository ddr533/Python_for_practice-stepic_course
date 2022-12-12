#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
text = form.getfirst("INPUT_TEXT", "не задано")
text = text[:-1]

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
        </head>
        <body>""")

for i in range(1, len(text) + 1, 2):
    print("<h1>" + str(hash(text[i])) + "</h1>")

print("""</body>
        </html>""")