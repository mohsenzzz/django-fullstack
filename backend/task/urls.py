from django.urls import path
from . import views



urlpatterns = [
    path('tasks',views.get_all_tasks,name='user_tasks'),
]