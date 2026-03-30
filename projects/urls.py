from django.urls import path
from . import views



urlpatterns = [
    path('view_all/', views.allprojects, name='view_all_projects'),
    path('create/', views.createproject, name='create_project'),
    path('view_one/<int:pk>/', views.oneproject, name='view_projects'),
    path('update/<int:pk>/', views.updateproject, name='update_project'),
    path('delete/<int:pk>/', views.deleteproject, name='delete_project'),
]