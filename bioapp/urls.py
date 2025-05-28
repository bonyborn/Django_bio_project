from django.urls import path
from . import views

app_name = 'bioapp'

urlpatterns = [
    path('create/', views.create_bio, name='create'),
    path('view/', views.view_bio, name='view'),
]
