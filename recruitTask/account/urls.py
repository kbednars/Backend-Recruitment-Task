from django.conf.urls import url
from .views import LoginView, LogoutView
from django.urls import path


urlpatterns = [path(r'login', LoginView.as_view()),
               path(r'logout', LogoutView.as_view())]