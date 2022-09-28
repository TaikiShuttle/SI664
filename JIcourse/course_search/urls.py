from django.urls import path
from . import views

namespace = "course_search"
urlpatterns = [
    path('', views.greet, name = 'greet'),
    path('search', views.Search.as_view(), name = 'search'),
    path('<slug:course_id>/', views.result, name = 'result'),
    path('add', views.Add.as_view(), name = "add"),
    path('add_success', views.add_success, name = "add_success"),
    path('add_fail', views.add_fail, name = "add_fail"),
]