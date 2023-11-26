from mptt.models import MPTTModel, TreeForeignKey
from django.db import models


class Category(MPTTModel):
    title = models.CharField('Название', max_length=255)
    parent = TreeForeignKey('Родитель', 'self', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Создан', auto_now_add=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title
