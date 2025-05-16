from django.urls import path
from . import views

urlpatterns = [
    path("", views.scheduling_mock_view, name="scheduling"),
]
