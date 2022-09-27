from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def index(request):
    test = '123'
    month = ['January', 'February', 'March', 'April', 'May', 'June',
             'July', 'August', 'September', 'October', 'November', 'December']
    # return render(request, 'front_end/pie_chart.html', locals())
    return render(request, 'front_end/column_chart.html', locals())
    # return render(request, 'front_end/line_chart.html', locals())

    # return HttpResponse('Hello world')


def show_column_chart(request):
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    data = [
        {'assets A': [random.random()*40 - 20 for x in range(12)]},
        {'assets B': [random.random()*40 - 20 for x in range(12)]},
        {'assets C': [random.random()*40 - 20 for x in range(12)]},
    ]

    return render(request, 'front_end/column_chart.html', locals())


def show_line_chart(request):
    pass


def show_line_chart_2(request):
    pass


def show_pie_chart(request):
    pass