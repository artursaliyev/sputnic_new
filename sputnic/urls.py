from django.urls import path
from . import views as sputnic_views


app_name = 'sputnic'
urlpatterns = [
    path('', sputnic_views.IndexView.as_view(), name='index'),
    path('search/', sputnic_views.SputnicSearchView.as_view(), name='search'),
    path('detail/<int:pk>/', sputnic_views.SputnicDetailView.as_view(), name='detail'),
]

