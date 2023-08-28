from django.contrib.auth.views import LoginView, LogoutView


class UserLoginView(LoginView):
    template_name = "users/login.html"
