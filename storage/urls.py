from django.urls import path, include

from .views import upload_form, view_ai_models

urlpatterns = [
    path('',view_ai_models, name='view_model'),
    path('upload',upload_form, name='upload_ai_model'),
]