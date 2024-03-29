from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

@login_required
def AppView(request):
    return render(request, 'app.html')
