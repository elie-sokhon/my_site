from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.views.generic import TemplateView, ListView, DetailView
from django.views import View
from .forms import CommentForm, CustomUserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile

def contact_form(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        subject = request.POST['subject']  # Renamed for clarity
        send_mail(
            subject,  # Subject of the email
            message,  # Message content
            settings.EMAIL_HOST_USER,  # From email
            [email],  # To email
            fail_silently=False,
        )
    return render(request, 'MainPage/email.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("starting-page")  # Redirect to the home page on successful login
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'MainPage/login.html')


def logout(request):
    pass


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)# Save the user
            user.email = form.cleaned_data.get('email')
            user.save()
            Profile.objects.create(user=user)  # Create a Profile linked to this user
            login(request, user)  # Log in the user after registration
            return redirect('starting-page')  # Redirect to home page
    else:
        form = CustomUserCreationForm()
    return render(request, 'MainPage/register.html', {'form': form})


class StartingPageView(TemplateView):
    template_name = "MainPage/index.html"

class AllProductsView(ListView):
    template_name = "MainPage/all-products.html" 
    model = Product
    context_object_name = "products"

class ProductDetail(View):

    def get(self, request,slug):
        product = Product.objects.get(slug=slug)
        context = {
            "single_product": product,
            "comment_form": CommentForm(),
            "comments":product.comments.all(),
        }
        return render(request, "MainPage/product-detail.html",context)

    def post(self,request,slug):
        comment_form = CommentForm(request.POST)
        product = Product.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.product = product
            comment.save()
            return HttpResponseRedirect(reverse(("product-detail"), args=[slug]))
        
        context = {
            "single_product": product,
            "comment_form": CommentForm(),
            "comments":product.comments.all(),
        }
        return render(request, "MainPage/product-detail.html", context)





def about_us(request):
    return render(request, "MainPage/about-us.html")

# def starting_page(request):
#     return render(request, "MainPage/index.html")

# def all_products(request):
#     all_products = Product.objects.all()
#     return render(request, "MainPage/all-products.html",{
#         "products":all_products
#     })

# def product_detail(request,slug):
#     #identified_product = Product.objects.get(slug=slug)
#     identified_product = get_object_or_404(Product, slug=slug)
#     return render(request, "MainPage/product-detail.html", {
#         "single_product": identified_product
#     })



