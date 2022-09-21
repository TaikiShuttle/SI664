from django.urls import path
from . import views

namespace = "course_search"
urlpatterns = [
    path('', views.greet, name = 'greet'),
    path('<slug:course_id>/', views.result, name = 'result'),
]