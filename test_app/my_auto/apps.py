from django.apps import AppConfig


class MyAutoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_auto'
