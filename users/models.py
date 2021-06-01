from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class CostumerBaseManager(BaseUserManager):
    def create_user(self, email, username,firstname, lastname, password, contact, **other_fields):
        if not email:
            raise ValueError("Please provide email")
        email = self.normalize_email(email)
        user  = self.model(email=email, username=username, firstname=firstname, lastname=lastname, password=password,contact=contact, **other_fields)
        print(password)
        user.set_password(password)
        print(password)
        user.save()
        return user
    def create_superuser(self, email, username,firstname, lastname, password, contact, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must assign is_staff = True')
        
        return self.create_user(email, username, firstname, lastname, password, contact, **other_fields)



class Costumer(AbstractBaseUser, PermissionsMixin):
    email           = models.EmailField(_("email"),unique=True, blank=False)
    username       = models.CharField(max_length=100, unique=True, blank=False)
    firstname       = models.CharField(max_length=100, blank=False)
    lastname       = models.CharField(max_length=120, blank=False)
    start_date      = models.DateTimeField(default=timezone.now)
    about           = models.TextField(_("about me"), max_length=500, blank=True)
    investing_style = models.PositiveIntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(3)])
    contact         = models.CharField(max_length=11, blank=True)
    is_active       = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)

    objects = CostumerBaseManager()
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname', 'contact']

    def __str__(self):
        return self.username

    def get_username(self):
        return self.username

    def get_absolute_url(self):
        return reverse("pages:profile", kwargs={"username":self.username})
    def get_absolute_url_security(self):
        return reverse("pages:security", kwargs={"username":self.username})
    def get_absolute_url_update(self):
        return reverse("pages:update", kwargs={"username":self.username})