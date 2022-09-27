from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('column_chart/', views.show_column_chart),
    path('line_chart/', views.show_line_chart),
    path('line_chart_2/', views.show_line_chart_2),
    path('pie_chart/', views.show_pie_chart),
]