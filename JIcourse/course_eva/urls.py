from django.urls import path
from . import views

namespace = "course_eva"
urlpatterns = [
    path('', views.greet, name = 'greet')
]