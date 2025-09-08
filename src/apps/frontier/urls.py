from django.urls import path

from apps.frontier.apis.mustfailrequest import MustFailRequest
from apps.frontier.apis.rawrequest import RawRequest

from .apis.successrequest import SuccessRequest
from .apis.timeoutrequest import TimeoutRequest


urlpatterns = [
    path("api/success-request", SuccessRequest.as_view(), name="success_request"),
    path("api/timeout-request", TimeoutRequest.as_view(), name="timeout_request"),
    path("api/mustfail-request", MustFailRequest.as_view(), name="must_fail_request"),
    path("api/raw-request", RawRequest.as_view(), name="must_fail_request"),
]
