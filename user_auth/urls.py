from django.urls import path
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('show_index/', views.show_index, name='show_index'),
    path('register_user/', views.register_user, name='register_user'),
    path("logout", views.logout_request, name= "logout"),
]