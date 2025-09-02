import asyncio

from rest_framework import response, status, views

from apps.sharedapp.services.sendrequest import CircuitBreakerError, SendRequestService


class ProxyRequest(views.APIView):
    service: SendRequestService = None

    def get(self, request, *args, **kwargs):
        try:
            nocb = request.GET.get('non_circuit_breaker', False)
            return response.Response(
                data=asyncio.run(self.service.send(nocb=nocb)),
                status=status.HTTP_200_OK,
                content_type="application/json",
            )
        except CircuitBreakerError:
            return response.Response(
                {"error": "Circuit is opened"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )
        except Exception as ex:
            # Lỗi tức thời khi CLOSED/HALF-OPEN
            return response.Response(
                {"error": str(ex)},
                status=status.HTTP_502_BAD_GATEWAY,
            )
