from django.urls import path
from . import views

urlpatterns = [
    # Commented out to avoid conflict with users app vaccination view
    # path("", views.vaccination_mock_view, name="vaccination"),
]
