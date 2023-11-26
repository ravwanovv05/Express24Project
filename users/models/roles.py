from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Role(models.Model):
    title = models.CharField('Название', max_length=255, null=True, blank=True)
    created_at = models.DateTimeField('Создан', auto_now_add=True)

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Ролы'


class UserRole(models.Model):
    user = models.OneToOneField('Пользователь', User, on_delete=models.CASCADE)
    role = models.ForeignKey('Роль', Role, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Создан')

    class Meta:
        verbose_name = 'Пользователь и роль'
        verbose_name_plural = 'Пользователи и роли'
