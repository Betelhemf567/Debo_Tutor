from django.urls import path
from . import views

urlpatterns = [
    path('', views.resource_list, name='resource_list'),
    path('upload/', views.resource_upload, name='resource_upload'),
    path('resource/<int:pk>/', views.resource_detail, name='resource_detail'),
    path('download/<int:pk>/', views.resource_download, name='resource_download'),
]
