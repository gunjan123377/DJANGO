from django.urls import path
from . import views

urlpatterns=[
	path("",views.home, name="HOME"),
	path("add",views.add, name="add")
]