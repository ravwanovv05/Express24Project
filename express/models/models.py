from django.contrib.auth import get_user_model
from mptt.models import MPTTModel, TreeForeignKey
from django.db import models

User = get_user_model()


class Category(MPTTModel):
    title = models.CharField('Название', max_length=255)
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Создан', auto_now_add=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField('Название', max_length=255, null=True, blank=True)
    image = models.ImageField('Изображение', upload_to='pics')
    price = models.DecimalField('Цена', max_digits=255, decimal_places=2, null=True, blank=True)
    description = models.TextField('Описание', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Создан', auto_now_add=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


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


class CommentToOrder(models.Model):
    text = models.TextField('Комментарий', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f"{self.pk}"

