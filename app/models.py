from django.db import models

# Прописываем модель товара


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    material = models.CharField(max_length=20, verbose_name="Материал")
    price = models.PositiveIntegerField(verbose_name="Цена")
    count = models.PositiveIntegerField(verbose_name="Количество")
    produced = models.CharField(max_length=20, verbose_name="Произведён")

    def __str__(self):
        return f"{self.title} {self.price}"

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
