from django.contrib.auth.base_user import BaseUserManager
# from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models

# import datetime


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Keeps users information."""
    username = None
    email = models.EmailField(
        verbose_name='Имеил пользователя',
        max_length=150,
        unique=True
    )
    password = models.CharField(
        verbose_name='Пароль пользователя',
        max_length=50
    )
    mobile_phone = models.CharField(
        verbose_name='Телефон пользователя',
        max_length=50,
        blank=True
    )
    first_name = models.CharField(
        verbose_name='Имя пользователя',
        max_length=100,
        blank=True
    )
    last_name = models.CharField(
        verbose_name='Фамилия пользователя',
        max_length=100,
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return f'Пользователь: {self.first_name} {self.last_name}'


class BannedUser(models.Model):
    "Keeps user's bannes info."

    user_banned = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='banning'
    )
    is_locked = models.BooleanField(default=False)
    date_locked = models.DateTimeField(
        verbose_name='Дата бана пользователя',
        blank=True,
        null=True
    )
    date_unlocked = models.DateTimeField(
        verbose_name='Дата снятия бана с пользователя',
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        if self.is_locked:
            return (f'{self.user_banned} '
                    f'is_locked = {self.is_locked} {self.date_locked}')
        return f'{self.user_banned} is_locked = {self.is_locked}'

    # def lock_user(self):
    #     self.is_banned = True
    #     self.date_locked = datetime.datetime().now()
    #     return ('Пользватель с имейлом'
    #             f'{self.email} заблокирован {self.date_locked}')

    # def unlock_used(self):
    #     self.is_banned = False
    #     self.date_unlocked = datetime.datetime().now()
    #     return ('Пользватель с имейлом'
    #             f'{self.email} разблокирован {self.date_locked}')
