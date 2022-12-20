from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
# Create your models here.

class WorkflowUserManager(BaseUserManager):
    
    def create_superuser(self,email, firstName, lastName,password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')
        super_user = self.create_user(email, firstName, lastName, password, **other_fields)
        return super_user
    
    def create_user(self,email, firstName, lastName, password, **other_fields):
        if not email:
            raise ValueError("Must be Email")
        email = self.normalize_email(email)
        user = self.model(email = email, firstName= firstName, lastName=lastName, **other_fields)
        user.set_password(password)
        user.save()
        return user


class WorkflowUser(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('','Choose Gender'),
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    )

    email = models.EmailField('email_address',unique=True)
    firstName = models.CharField(max_length=150, blank=True)
    lastName = models.CharField(max_length=150, blank=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = WorkflowUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName', 'lastName']

    def __str__(self):
        return f"{self.firstName}{self.lastName}"