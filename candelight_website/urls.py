from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexPageView.as_view(), name="main_page"),
    path("about-us", views.AboutPageView.as_view(), name="about_page")
]
