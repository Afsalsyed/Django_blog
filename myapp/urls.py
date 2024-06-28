from django.urls import path
from . import views
urlpatterns =[
    path("first/", views.home, name="home"),
    path("post/<str:slug>", views.detail , name="detail")
]