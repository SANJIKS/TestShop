from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def _create(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Укажите email!')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        return self._create(email, password, **extra_fields)

    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        return self._create(email, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = 'username' 
    REQUIRED_FIELDS = ['email']

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, obj=None):
        return self.is_staff
    

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    def __str__(self):
        return self.email