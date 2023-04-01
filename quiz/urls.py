from django.urls import path
from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:quiz_id>/', views.topic, name='topic'),
    path('<int:quiz_id>/results/', views.results, name='results'),
]