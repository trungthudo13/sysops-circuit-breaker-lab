from apps.sharedapp.consts import APIs

from .sendrequest import SendRequestService


class TimeoutRequestService(SendRequestService):
    @property
    def get_timeout_request_api(self):
        return f"{self._domain_name}/{APIs.TIMEOUT_REQUEST_API.value}"

    def __init__(self, domain_name: str, *args, **kwargs):
        super().__init__(domain_name, *args, **kwargs)

    def send_api(self):
        return self.get_timeout_request_api
