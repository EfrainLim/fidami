from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from pages.mixins import ElimnacionImagenes
class MyAccountManager(BaseUserManager):
    #crear cuenta tipo usuario
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('El usuario debe tener correo electrónico')
        if not username:
            raise ValueError('El usuario debe tener nombre de usuario')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    #crear cuenta tipo super usuario
    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

#cuenta
class Account(AbstractBaseUser,PermissionsMixin):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    phone_number    = models.CharField(max_length=50)

    # requerido
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active        = models.BooleanField(default=False)
    is_superadmin        = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, add_label):
        return True

#perfil de usuario
class PerfilUsuario(ElimnacionImagenes):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    direccion_1 = models.CharField(blank=True, max_length=100)
    direccion_2 = models.CharField(blank=True, max_length=100)
    foto_perfil = models.ImageField(blank=True, upload_to='perfilusuario')
    ciudad = models.CharField(blank=True, max_length=20)
    estado = models.CharField(blank=True, max_length=20)
    pais = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.user.first_name

    def direccion_completa(self):
        return f'{self.direccion_1} {self.direccion_2}'