# models.py
from datetime import timezone

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    depth = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(Category, related_name='products')
    views_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Video(models.Model):
    product = models.ForeignKey(Product, related_name="videos", on_delete=models.CASCADE)
    video_url = models.URLField(blank=True, null=True)


class Image(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


class DiscountCode(models.Model):
    CODE_TYPES = (
        ('percentage', 'Percentage'),
        ('fixed_amount', 'Fixed Amount'),
    )
    code = models.CharField(max_length=20, unique=True)
    discount_type = models.CharField(max_length=20, choices=CODE_TYPES)
    limit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    products = models.ManyToManyField(Product, related_name='discount_codes')
    categories = models.ManyToManyField(Category, related_name='discount_codes')

    def __str__(self):
        return self.code


class PriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} - {self.price} ({self.timestamp})"

#
# class User(AbstractBaseUser):
#     username = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)
#
#     def __str__(self):
#         return f"{self.username}"

# class UserManager(BaseUserManager):
#     def create_user(self, email, username, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self.create_user(email, username, password, **extra_fields)
# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=100, unique=True)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)
#     date_joined = models.DateTimeField(default=timezone.max)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#
#     def __str__(self):
#         return self.username


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', related_name='carts')
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Cart for {self.user}"


class Banner(models.Model):
    BANNER_TYPES = (
        ('head_banner', 'HeadBanner'),
        ('ad_banner', 'AdBanner'),
    )
    banner_type = models.CharField(max_length=50, default="null", choices=BANNER_TYPES)
    title = models.CharField(max_length=100, default="null")
    description = models.TextField(default="null")
    image = models.ImageField(upload_to='banners/')
    button_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.banner_type}"

