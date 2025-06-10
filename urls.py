from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from vaccination import views as vaccination_views

urlpatterns = [
    # Core routes
    path('', user_views.home_view, name='home'),
    path('admin/', admin.site.urls),
    path('login/', user_views.login_view, name='login'),
    
    # Vaccination routes
    path('ubs/<str:ubs_name>/', vaccination_views.ubs_detail_view, name='ubs_detail'),
    
    # API routes
    path('api/users/', include('users.urls')),
    path('api/scheduling/', include('scheduling.urls')),
    path('api/chat/', include('chat.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/administration/', include('administration.urls')),
    path('api/reports/', include('reports.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
