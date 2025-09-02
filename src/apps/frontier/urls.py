from django.urls import path

from .apis.successrequest import SuccessRequest
from .apis.timeoutrequest import TimeoutRequest


urlpatterns = [
    path("api/success-request", SuccessRequest.as_view(), name="success_request"),
    path("api/timeout-request", TimeoutRequest.as_view(), name="timeout_request"),
]
