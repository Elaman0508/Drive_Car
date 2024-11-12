from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, full_name=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, full_name=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, full_name, **extra_fields)

# User Model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    # Adding related_name to avoid conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Unique name for reverse relation
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Unique name for reverse relation
        blank=True,
    )

# Model for Verification Code
class VerificationCode(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email} - {self.code}'


