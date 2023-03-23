from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('<int:num>/', views.detail, name='detail'),
    path('hello/<str:name>/', views.greeting, name='greeting'),
]