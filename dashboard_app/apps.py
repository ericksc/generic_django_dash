from django.apps import AppConfig

class DashboardAppConfig(AppConfig):
    name = 'dashboard_app'

    def ready(self):
        import dashboard_app.dash_app  # register Dash app
