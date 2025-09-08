from .sendrequest import SendRequestService


class RawRequestService(SendRequestService):
    @property
    def get_raw_request_api(self):
        return f"{self._domain_name}"

    def __init__(self, domain_name: str, *args, **kwargs):
        super().__init__(domain_name, *args, **kwargs)

    def send_api(self):
        return self.get_raw_request_api
