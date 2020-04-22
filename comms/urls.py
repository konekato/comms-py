from django.urls import path
 
from . import views

app_name = 'comms'
 
urlpatterns = [
    path('home/', views.home, name='home'),
    path('<str:username>/', views.user_articles, name='user_articles'),
    path('<str:username>/status/<int:article_id>/', views.user_article, name='user_article'),
    path('compose/article/', views.create_user_article, name='create_user_article'),
]