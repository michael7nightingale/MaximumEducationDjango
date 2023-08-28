from django.urls import path

from .views import UserLoginView, user_logout, UserRegisterView


urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("logout/", user_logout, name="logout"),

]
