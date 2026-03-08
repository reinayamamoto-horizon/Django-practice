from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('article/<int:pk>/', views.post_article, name='post_article'),
    path('article/<int:pk>/edit/', views.editor_article, name='editor_article'),
    path('article/<int:pk>/delete/', views.delete_article, name='delete_article'),
    path('create/', views.create_article, name='create_article'),
]