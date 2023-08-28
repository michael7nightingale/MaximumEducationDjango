from django.contrib.auth.views import LoginView, FormView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse, redirect

from .forms import UserLoginForm, UserRegisterForm


class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse("home")


class UserRegisterView(FormView):
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = "/users/login"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse("home"))
