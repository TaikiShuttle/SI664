from django.urls import path
from . import views

namespace = 'main'
urlpatterns = [
    path('', views.main, name = 'main')
]
