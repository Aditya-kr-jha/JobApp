
from django.urls import path

from uploadapp import views


urlpatterns = [
    path('uploadStart/', views.uploadStart, name='uploadStart'),
    path('upload_form/', views.upload_form, name='upload_form'),
    path('upload_files/', views.upload_files, name='upload_files'),
]
