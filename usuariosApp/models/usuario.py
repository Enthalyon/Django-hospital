from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class AdministradorDeUsuarios(BaseUserManager):
    def crear_usuario(self, email, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not email:
            raise ValueError('Los usuarios deben tener un email')
        user = self.model(username=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    # def crear_administrador(self, email, password):
    #     """
    #     Creates and saves a superuser with the given username and password.
    #     """
    #     user = self.crear_usuario(
    #         username=email,
    #         password=password,
    #     )
    #     user.is_admin = True
    #     user.save(using=self._db)
    #     return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    password = models.CharField('Password', max_length = 256, null=False, default="Sin password")
    email = models.EmailField('Email', max_length =100, unique=True, null=False, default="Sin email")
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = AdministradorDeUsuarios()
    USERNAME_FIELD = 'email'