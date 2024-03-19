from django.contrib import admin

from app.models import Product

# Регистрируем модель в Админ панели

admin.site.register(Product)
