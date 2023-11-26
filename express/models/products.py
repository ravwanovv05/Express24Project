from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    title = models.CharField('Название', max_length=255, null=True, blank=True)
    price = models.DecimalField('Цена', max_length=255, null=True, blank=True)
    description = models.TextField('Описание', null=True, blank=True)
    category = models.ForeignKey('Категория', 'categories.Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField('Создан', auto_now_add=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class ShoppingCart(models.Model):
    count = models.PositiveIntegerField('Количество', null=True, blank=True, default=1)
    user = models.ForeignKey('Пользователь', User, on_delete=models.CASCADE)
    product = models.ForeignKey('Продукт', Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Создан', )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return self.pk
