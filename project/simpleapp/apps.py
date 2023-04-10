from django.apps import AppConfig
import redis


class SimpleAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'simpleapp'

    def ready(self):
        import simpleapp.signals


red = redis.Redis(
    host='redis-19490.c261.us-east-1-4.ec2.cloud.redislabs.com',
    port=19490,
    password='tstQL4uDjHq08UDUrE8DRUuFdG3wNgEX'
)
