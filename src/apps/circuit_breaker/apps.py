from django.apps import AppConfig


class CircuitBreakerConfig(AppConfig):
    name = 'apps.circuit_breaker'
    verbose_name = "Circuit Breaker"

    def ready(self):
        # Add System checks
        pass
