
from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='list'),
    path('<int:article_pk>/', views.article_detail, name='detail'),
]
