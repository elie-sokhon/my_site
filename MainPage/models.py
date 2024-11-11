from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user_name = models.CharField(max_length=100,null=True)
    email_address = models.EmailField(null=True)
    password1 = models.CharField(max_length=100, null=True)
    password2 = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.user_name}"
    
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    image_name = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    pdf_file = models.FileField(upload_to='MainPage/pdfs/', blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
    
class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    text = models.TextField(max_length=500)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically sets the date when the comment is created

    def __str__(self):
        return f"{self.user_name} - {self.text[:20]}"
    
