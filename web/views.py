from django.shortcuts import render, redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from dataclasses import dataclass

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('topics')
        return render(request, "login.html", {})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('topics')  # Redirect to the app view
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html', {})
@dataclass
class Topic:
    emoji_string : str
    label: str
    convo_count: int

class TopicView(View):
    @method_decorator(login_required)
    def get(self, request):
        topics = []
        topics.append(Topic("&#x1F9D1;&#x200D;&#x1F373;", "Cooking", 1))
        topics.append(Topic("&#x1F6F0;&#xFE0F", "Raspberry Pi", 4))
        topics.append(Topic("&#x1F426;", "Tweets", 6))
        return render(request, 'topics.html', {"topics": topics})
