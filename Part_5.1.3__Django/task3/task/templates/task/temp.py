v = [[1,2],[3,5]]

d = dict((i, f'url+{i}') for row in v for i in row)

print(d)