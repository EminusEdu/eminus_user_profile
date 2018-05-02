from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class MyUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not email:
            raise ValueError('The given Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class MyUser(AbstractBaseUser, PermissionsMixin):
    # ==========AbstractBaseUser's fields==========
    # password = models.CharField(_('password'), max_length=128)
    # last_login = models.DateTimeField(_('last login'), blank=True, null=True)
    # is_active = True

    # ===============Auth===============
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    # ===============Basic===============
    nick_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    birthday = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=20)

    # ===============Course===============
    time_zone = models.CharField(max_length=20, blank=True)
    mother_language = models.CharField(max_length=20)
    # second_language => store in SecondLanguage

    # ===============Foreign===============
    # wallet_id = models.CharField(max_length=30)
    # facebook
    # google

    # ===============Status===============
    is_teacher = models.BooleanField(
        'teacher status',
        default=False,
        help_text='Whether the user can teach course in this website.',
    )
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )

    # ===============Setting===============
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nick_name', 'country', 'mother_language', ]
    objects = MyUserManager()
