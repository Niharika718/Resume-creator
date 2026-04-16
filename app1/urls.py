from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_resume, name='create'),
    path('list/', views.resume_list, name='resume_list'),
    path('download/<int:id>/', views.download_resume, name='download_resume'),
    path('edit/<int:id>/', views.update_resume, name='update_resume'),
    path('delete/<int:id>/', views.delete_resume, name='delete_resume'),
]