from django.core.exceptions import ValidationError
from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    picture = models.ImageField('Foto', upload_to='user_profile')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    
    class Meta:
        verbose_name= 'Perfil do Usuário'
        verbose_name_plural = 'Perfis dos Usuários'
        
    def __str__(self):
        return self.user.username

    # def clean(self):
    #     model = self.__class__
    #     if model.objects.count() > 0 and self.id != model.objects.get().id:
    #         raise ValidationError("Já existe um perfil cadastrado para este usuário!")