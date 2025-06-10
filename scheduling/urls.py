from django.urls import path
from . import views

urlpatterns = [
    path("", views.scheduling_view, name="scheduling"),
]
