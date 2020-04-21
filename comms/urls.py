from django.urls import path
 
from . import views

app_name = 'comms'
 
urlpatterns = [
    path('home/', views.home, name='home'),
    path('<str:username>/', views.user_articles, name='user_articles'),
    path('<str:username>/status/<int:article_id>/', views.user_article, name='user_article'),
    path('create/', views.create, name='create'),
]