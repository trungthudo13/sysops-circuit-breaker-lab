from apps.sharedapp.consts import APIs

from .sendrequest import SendRequestService


class SuccessRequestService(SendRequestService):
    @property
    def get_success_request_api(self):
        return f"{self._domain_name}/{APIs.SUCCESS_REQUEST_API.value}"

    def __init__(self, domain_name: str, *args, **kwargs):
        super().__init__(domain_name, *args, **kwargs)

    def send_api(self):
        return self.get_success_request_api
