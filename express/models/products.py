from django.db import models
from django.contrib.auth import get_user_model

from express.models.categories import Category

User = get_user_model()


class Product(models.Model):
    title = models.CharField('Название', max_length=255, null=True, blank=True)
    price = models.DecimalField('Цена', max_digits=255, decimal_places=2, null=True, blank=True)
    description = models.TextField('Описание', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Создан', auto_now_add=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class Picture(models.Model):
    image = models.ImageField('Изображение', upload_to='pics')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Создан', auto_now_add=True)

    class Meta:
        verbose_name = 'Картина'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return f"{self.pk}"


class ShoppingCart(models.Model):
    count = models.PositiveIntegerField('Количество', null=True, blank=True, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Создан', auto_now_add=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f"{self.pk}"
