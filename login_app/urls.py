from django.urls import path     
from . import views

app_name = "main"
urlpatterns = [
    path('register', views.register_page , name="register"),	   
    path('login', views.login_page , name="login"),	
    # path('logout', views.log_out , name = 'log_out'),
]