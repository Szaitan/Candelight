from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexPageView.as_view(), name="main_page"),
    path("about-us", views.AboutPageView.as_view(), name="about_page"),
    path("realisations", views.RealisationsPageView.as_view(), name="realisations_page"),
    path("realisations/<slug:slug>", views.RealisationPageView.as_view(), name="realisation_page"),
    path("get_realizations/<int:type_id>/", views.get_realizations, name="get_realizations"),
    path("contact", views.ContactPageView.as_view(), name="contact_page"),
    path("products", views.ProductsPageView.as_view(), name="products_page"),
    path("get_products/<str:type_id>/", views.get_products, name="get_products"),
]

