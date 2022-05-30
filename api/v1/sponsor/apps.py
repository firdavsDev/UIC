from django.apps import AppConfig


class SponsorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.v1.sponsor'

    def ready(self):
        import api.v1.sponsor.signals