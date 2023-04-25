
from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='list'),
    path('<int:article_pk>/', views.article_detail, name='detail'),
    path('comments/', views.comment_list, name='comment_list'),
    path('comments/<int:comment_pk>/', views.comment_detail, name='comment_detail'),
    path('<int:article_pk>/comments/', views.comment_create, name='comment_create'),
]
