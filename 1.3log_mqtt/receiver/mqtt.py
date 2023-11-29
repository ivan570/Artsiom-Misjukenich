import paho.mqtt.client as mqtt
from django.conf import settings


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(settings.MQTT_TOPIC)


def on_message(client, userdata, msg):
    print(msg)
    payload = msg.payload.decode("utf-8")
    print(f"Received message on topic {msg.topic}: {payload}")


def start_mqtt_client():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(settings.MQTT_BROKER, settings.MQTT_PORT, 60)

    client.loop_start()
