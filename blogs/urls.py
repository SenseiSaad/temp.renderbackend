from django.urls import path
from . import views

urlpatterns = [
    path('view_all/', views.view_all_blogs, name='view_all_blogs'),
    path('create/', views.create_blog, name='create_blog'),
    path('view_one/<int:pk>/', views.view_blog, name='view_blog'),
    path('update/<int:pk>/', views.update_blog, name='update_blog'),
    path('delete/<int:pk>/', views.delete_blog, name='delete_blog'),
]