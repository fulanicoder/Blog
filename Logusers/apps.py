from django.apps import AppConfig


class LogusersConfig(AppConfig):
    name = 'Logusers'

    def ready(self):
        
        import Logusers.signals
