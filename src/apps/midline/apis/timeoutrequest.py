from django.conf import settings

from apps.sharedapp.apis.proxyrequest import ProxyRequest
from apps.sharedapp.services.timeoutrequest import TimeoutRequestService


class TimeoutRequest(ProxyRequest):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = TimeoutRequestService(settings.BACKLINE_DOMAIN)
