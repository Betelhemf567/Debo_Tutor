from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home  # Import the new view
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('discussions/', include('discussions.urls')),
    path('resources/', include('resources.urls')),
    path('profiles/', include('profiles.urls')),
    path('accounts/login/', LoginView.as_view(template_name='authentication/login.html'), name='login'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
