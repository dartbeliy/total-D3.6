from django.urls import path
from .views import detail, default
# from .views import index, detail, default

urlpatterns = [
    path('', default, name='default'),
    path('new/<str:slug>', detail, name='detail'),
]