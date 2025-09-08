from apps.sharedapp.consts import APIs

from .sendrequest import SendRequestService


class MustFailService(SendRequestService):
    @property
    def get_mustfail_request_api(self):
        return f"{self._domain_name}/{APIs.MUSTFAIL_REQUEST_API.value}"

    def __init__(self, domain_name: str, *args, **kwargs):
        super().__init__(domain_name, *args, **kwargs)

    def send_api(self):
        return self.get_mustfail_request_api
