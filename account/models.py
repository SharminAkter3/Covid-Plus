from django.db import models
from django.contrib.auth.models import User


ROLE_CHOICES = [
    ("Patient", "Patient"),
    ("Doctor", "Doctor"),
]

GENDER_TYPES = [
    ("Male", "Male"),
    ("Female", "Female"),
]


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    nid = models.CharField(max_length=20, unique=True, verbose_name="National ID")
    birth_date = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="Patient")
    gender = models.CharField(
        max_length=10, choices=GENDER_TYPES, blank=True, null=True
    )
    street_address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.role} :  {self.user.username} - {self.nid}"
