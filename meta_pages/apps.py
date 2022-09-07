from django.apps import AppConfig


class MetaPagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "meta_pages"
    label: str = 'meta_pages'
    verbose_name: str = 'Meta Pages'