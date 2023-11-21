from django.urls import path
from .views import update_catalog, home

urlpatterns = [
    path('update_catalog/', update_catalog, name='update_catalog'),
    path('home/',home, name='home'),
    ]