from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_task, name="create_task"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout_view, name="logout"),

]
