from django.shortcuts import render, redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('app')
        return render(request, "login.html", {})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('app')  # Redirect to the app view
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html', {})

class AppView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'app.html')
