from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_resume, name='create'),
    path('list/', views.resume_list, name='resume_list'),
    path('resume/<int:id>/', views.resume_detail, name='resume_detail'),
    path('edit/<int:id>/', views.update_resume, name='update_resume'),
    path('delete/<int:id>/', views.delete_resume, name='delete_resume'),
]