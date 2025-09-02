from time import sleep

from rest_framework import response, status, views

from apps.backline.services.unstable import UnstableException, UnstableService


class TimeoutRequest(views.APIView):
    service: UnstableService = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = UnstableService()

    def get(self, request, *args, **kwargs):
        try:
            return response.Response(
                data=self.service.get,
                status=status.HTTP_200_OK,
                content_type="application/json",
            )
        except UnstableException as ex:
            print(ex, end=" - Status failed\n")
            return response.Response(
                data=str(ex),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content_type="application/json",
            )
