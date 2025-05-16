from django.urls import path
from . import views

from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("login/", views.login_view, name="login"),
    path("ubs-proximas/", views.nearby_ubs_view, name="ubs_nearby"),
    path("vacinação/", views.vaccination_view, name="vaccination"),
]
