from django.contrib import admin
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home_view, name='home'),
    path('login/', user_views.login_view, name='login'),
    path('api/users/', include('users.urls')),
    path('api/scheduling/', include('scheduling.urls')),
    path('api/vaccination/', include('vaccination.urls')),
    path('api/chat/', include('chat.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/administration/', include('administration.urls')),
    path('api/reports/', include('reports.urls')),
]
