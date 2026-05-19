from django.contrib import admin
from django.urls import path, include  # <-- O 'include' precisa estar aqui
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pets.urls')), # <-- Esta linha redireciona para a nossa Home
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)