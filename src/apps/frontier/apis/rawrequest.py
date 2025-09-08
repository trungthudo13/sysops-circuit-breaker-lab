from django.conf import settings

from apps.sharedapp.apis.proxyrequest import ProxyRequest
from apps.sharedapp.services.rawrequest import RawRequestService


class RawRequest(ProxyRequest):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = RawRequestService(settings.MIDLINE_DOMAIN)

    # def get(self, request, *args, **kwargs):
    #     return super().get(request=request, *args, **kwargs)
