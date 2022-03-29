from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Email inválido')
        u = self.model(email=self.normalize_email(email), **kwargs)
        u.set_password(password)
        u.save()
        return u

    def create_superuser(self, email, password, **kwargs):
        u = self.create_user(email, password, **kwargs)
        u.is_superuser = True
        u.save()
        return u

class AbstractBaseModel(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class UsuarioAbstract(AbstractBaseUser, AbstractBaseModel):
    email = models.EmailField('Email', unique=True, blank=False, null=False)
    password = models.CharField('Senha', blank=False, null=False, max_length=250)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField('Nome', max_length=100, blank=True, null=True)
    last_name = models.CharField('Sobrenome', max_length=100, blank=True, null=True)
    nickname = models.CharField('Nickname', max_length=100, blank=True, null=True, unique=True)
    is_superuser = models.BooleanField('Superusuário', default=False)
    photo = models.TextField('Imagem de perfil (Base64)', blank=True, null=True)
    
    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return '{0} {1}({2})'.format(self.first_name, self.last_name, self.nickname)

    @property
    def is_staff(self):
        return self.is_superuser

    @property
    def fullname(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        abstract = True

class Usuario(UsuarioAbstract):
    
    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'