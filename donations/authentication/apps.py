from django.apps import AppConfig


class GraphQLAuthConfig(AppConfig):
    name = "authentication"
    verbose_name = "authentication"

    def ready(self):
        import authentication.signals
