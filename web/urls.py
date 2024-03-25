from django.urls import path
from web.views import LoginView

urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
]

