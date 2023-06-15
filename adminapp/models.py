from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager





# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


class Department(models.Model): 
    name = models.CharField(max_length=50, null=False)
    create_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="department_created_by")
    create_date = models.DateTimeField(auto_now_add=True)
    update_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="department_updated_by")
    update_date = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=50, null=False)
    create_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="category_created_by")
    create_date = models.DateTimeField(auto_now_add=True)
    update_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="category_updated_by")
    update_date = models.DateTimeField(auto_now=True)

