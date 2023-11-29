from django.apps import AppConfig


class MqttReceiverConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "receiver"

    def ready(self):
        from .mqtt import start_mqtt_client

        start_mqtt_client()
