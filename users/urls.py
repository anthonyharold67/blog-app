
from django.urls import include, path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import register, user_login, user_logout, user_profile

urlpatterns = [
    path("login/",user_login,name="user_login"),
    path("register/",register,name="register"),
    path("logout/", user_logout, name="user_logout"),
    path("profile/",user_profile,name="user_profile"),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='users/reset-password.html',success_url=reverse_lazy('reset_done')), name='reset-password'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_done.html'), name='reset_done'),
]