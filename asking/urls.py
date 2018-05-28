from django.urls import path
from asking import views

app_name = "question" #registed namespace
urlpatterns = [
	path('<str:username>', views.IndexView , name = 'index'),
	
]
