from django.urls import path
from . import views as sputnic_views


app_name = 'sputnic'
urlpatterns = [
    path('', sputnic_views.index, name='index'),

]

