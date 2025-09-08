from time import sleep

from rest_framework import response, status, views

from apps.backline.services.unstable import UnstableException, UnstableService


class MustFailRequest(views.APIView):

    def get(self, request, *args, **kwargs):
        try:
            return response.Response(
                data=None,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content_type="application/json",
            )
        except UnstableException as ex:
            print(ex, end=" - Status failed\n")
            return response.Response(
                data=str(ex),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content_type="application/json",
            )
