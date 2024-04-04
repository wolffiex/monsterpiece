from django.urls import path
from web.views import LoginView, TopicView

urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("topics", TopicView.as_view(), name="topics"),
]

