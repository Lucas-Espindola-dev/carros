from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'

    # Esta função significa inicializando os signals, está pronto.
    def ready(self):
        import cars.signals
