from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("settings/", views.settings, name="settings"),
    path("logout/", views.logout_view, name="logout"),
]