from django.urls import path
from clima.views import index

urlpatterns = [
    path('', index, name='index')
]