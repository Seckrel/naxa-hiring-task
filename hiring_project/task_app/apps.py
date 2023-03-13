from django.apps import AppConfig
from django.core.signals import setting_changed



class TaskAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task_app'

    def ready(self) -> None:
        from .signals import validate_project
        from .models import Project

        setting_changed.connect(validate_project, sender=Project)