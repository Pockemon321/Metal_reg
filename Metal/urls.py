
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
import app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("app.urls"))
] 

# поднастройка для статических файлов
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
