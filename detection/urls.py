from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('output',views.output, name='output'),
    path('download',views.output, name='download'),

]