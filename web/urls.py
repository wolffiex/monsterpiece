from django.urls import path
from web.views import LoginView, TopicView, ThreadsView
from django.shortcuts import redirect

def root_redirect(request):
    if request.user.is_authenticated:
        return redirect('topics')
    else:
        return redirect('login')

urlpatterns = [
    path("", root_redirect, name="index"),
    path("login", LoginView.as_view(), name="login"),
    path("topics", TopicView.as_view(), name="topics"),
    path("topics/<int:id>", ThreadsView.as_view(), name="threads"),
]
