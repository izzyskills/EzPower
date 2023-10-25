from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from . import models, forms
from django.urls import reverse_lazy
from django.contrib.auth import login, logout


# Create your views here.
class RegistrationView(CreateView):
    form_class = forms.UserCreationForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("login")


def login_view(request):
    if request.method == "POST":
        form = forms.LoginForm(request, request.POST)
        if form.is_valid():
            # Authenticate the user
            user = form.get_user()
            if user is not None and user.is_active:
                login(request, user)
                return redirect("home")  # Replace with the actual success URL

    else:
        form = forms.LoginForm()

    return render(request, "registration/login.html", {"form": form})


def logout_view(request):
    logout(request)  # Log the user out
    return redirect("home")


def home_view(request):
    return render(request, "home.html")
