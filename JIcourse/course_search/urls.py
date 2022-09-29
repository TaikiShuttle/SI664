from django.urls import path
from . import views

app_name = "course_search"
urlpatterns = [
    path('', views.greet, name = 'greet'),
    path('search', views.Search.as_view(), name = 'search'),
    path('<slug:course_id>/', views.result, name = 'result'),
    path('add', views.Add.as_view(), name = "add"),
    path('add_success', views.add_success, name = "add_success"),
    path('add_fail', views.add_fail, name = "add_fail"),
    path('course_list', views.course_list, name = 'course_list'),
]