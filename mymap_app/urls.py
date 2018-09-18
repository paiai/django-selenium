from django.urls import path
from . import views

app_name = 'mymap_app' 
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:addr>', views.lat_lon, name='lat_lon'),
    path('<int:id>', views.index_int, name='index_int'),
]