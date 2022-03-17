from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.index),  #127.0.0.1:8000/
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('common/', include('common.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


