from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),  # This must come BEFORE the username pattern
    path('profiles/profile/<str:username>/', views.profile_view, name='profile_view'),
]
