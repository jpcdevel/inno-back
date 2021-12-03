from django.db import models
from django.contrib.auth.models import AbstractUser

class ExtendedUser(AbstractUser):
    email = models.EmailField(blank=False, unique=True, max_length=255, verbose_name='User Email')
    type = models.CharField(max_length=10)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"


class Enquiry(models.Model):
    description = models.CharField(max_length=1000, db_column='description')
    occurrence = models.CharField(max_length=1000, db_column='occurence')
    try_resolve_example = models.CharField(max_length=1000, db_column='try_resolve_example')
    expiration_date =  models.DateTimeField(db_column='expiration_date')
    requisite_customer = models.CharField(max_length=1000, db_column='requisite_customer')
