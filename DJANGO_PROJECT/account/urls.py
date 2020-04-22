from django.urls import path
from . import views

urlpatterns=[
	path("register",views.register, name="REGISTER"),
	path("login",views.login, name="LOGIN"),
	path("logout",views.logout, name="LOGOUT")
]