from django.urls import path
from . import views

app_name = 'vaccination'

urlpatterns = [
    path('ubs/<str:ubs_name>/', views.ubs_detail_view, name='ubs_detail'),
    # Commented out the API path temporarily to fix the error
    # path('api/', views.get_vaccines_api, name='vaccines-api'),
]
