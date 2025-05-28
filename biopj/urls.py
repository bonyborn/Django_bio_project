from django.contrib import admin
from django.urls import path, include
from bioapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bio/create/', views.create_bio, name='create_bio'),
    path('bio/view/', views.view_bio, name='view_bio'),
    path('', views.view_bio, name='home')
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0]) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)