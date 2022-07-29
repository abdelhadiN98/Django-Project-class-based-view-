from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# class UserManager(BaseUserManager):
#     def create_superuser(self, email, username, password=None, **extra_fields):
#         if not email:
#             raise ValueError("User must have an email")
#         if not password:
#             raise ValueError("User must have a password")
#         if not username:
#             raise ValueError("User must have a full name")

#         user = self.model(
#             email=self.normalize_email(email)
#         )
#         user.full_name = username
#         user.set_password(password)
#         user.admin = True
#         user.staff = True
#         user.active = True
#         user.save(using=self._db)
#         return user


class Employee(AbstractUser):
    username = models.CharField(max_length=255,unique=True, null=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255,unique=True)
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.first_name + " " + self.last_name

class Customer(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    managed_by = models.ForeignKey(Employee , related_name="customers_managed", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Service(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    managed_by = models.ForeignKey(Employee , related_name="services_managed", on_delete = models.CASCADE)
    customers_have_servives = models.ManyToManyField(Customer , related_name="have_services")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("Employee_detail", kwargs={"pk": self.pk})
