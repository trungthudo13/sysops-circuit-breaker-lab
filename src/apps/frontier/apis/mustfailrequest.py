from django.conf import settings

from apps.sharedapp.apis.proxyrequest import ProxyRequest
from apps.sharedapp.services.mustfailrequest import MustFailService


class MustFailRequest(ProxyRequest):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = MustFailService(settings.MIDLINE_DOMAIN)
