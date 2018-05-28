from django.urls import path
from login import views

app_name = "authentication" #registed namespace
urlpatterns = [
	path('', views.login1 , name = 'login'),
	path('signup/', views.signup1, name = 'signup'),
	
]
