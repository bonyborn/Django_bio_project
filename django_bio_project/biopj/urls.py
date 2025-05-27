from django.contrib import admin
from django.urls import path
from bio_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bio/create/', views.create_bio, name='create_bio'),
    path('bio/view/', views.view_bio, name='view_bio'),
]