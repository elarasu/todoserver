from importlib import import_module

from django.apps import AppConfig as BaseAppConfig
from . import mqtt

class AppConfig(BaseAppConfig):

    name = "todoserver"

    def ready(self):
        import_module("todoserver.receivers")
        mqtt.init_mqtt()
