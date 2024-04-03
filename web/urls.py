from django.urls import path
from web.views import LoginView, AppView

urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("app", AppView.as_view(), name="app"),
]

