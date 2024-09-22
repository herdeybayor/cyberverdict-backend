from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class CustomUserManager(BaseUserManager):
    """Custome user manager."""

    def create_user(self, email, password=None, **extra_kwargs):
        if not email:
            raise ValueError("The Email field must be set.")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model representing user in the system."""

    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        """Return string representation of the object."""
        return self.email

    def has_perm(self, perm, obj=None):
        """Check if the user have a specific permission."""
        # Simplest possible answer: Yes, always
        return self.is_staff

    def has_module_perms(self, app_label):
        """Check if the user have permissions to view the app `app_label."""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_name_added(self):
        return self.first_name and self.last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
