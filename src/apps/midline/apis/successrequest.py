from django.conf import settings

from apps.sharedapp.apis.proxyrequest import ProxyRequest
from apps.sharedapp.services.successrequest import SuccessRequestService


class SuccessRequest(ProxyRequest):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = SuccessRequestService(settings.BACKLINE_DOMAIN)
