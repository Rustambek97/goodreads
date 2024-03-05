from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings


urlpatterns = [
    path('', include('books.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)