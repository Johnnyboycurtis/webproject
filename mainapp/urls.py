from django.urls import path

from mainapp import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('export/', views.export, name='export'),

]