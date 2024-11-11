from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.StartingPageView.as_view(), name = "starting-page"), 
    path("about-us",views.about_us, name = "about-us"),
    path("products",views.AllProductsView.as_view(), name = "all-products"),
    path("products/<slug:slug>", views.ProductDetail.as_view(), name = "product-detail"),
    path("register", views.register, name="register"),
    path("login", views.login , name="login"),
    path("logout", views.logout, name="logout"),
    path("email-us", views.contact_form, name="email"),
]



