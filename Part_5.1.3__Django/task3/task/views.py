from django.shortcuts import render

# Create your views here.

def index(request):
    values = [[j for j in range(i, i*10 + i, i)] for i in range(1,11)]
    url_dict = dict((i, f'http://{i}.ru') for row in values for i in row)

    return render(request, 'task/main.html', context={'table': values, 'urls': url_dict})
