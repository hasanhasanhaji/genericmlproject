from django.urls import path
from app.views import *

app_name = 'app'

urlpatterns = [
    path('', index_view, name='index'),
    path('predictdata/', predictdata_view, name='predictdata'),
]
