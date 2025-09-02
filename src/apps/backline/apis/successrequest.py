from rest_framework import response, status, views

from apps.backline.services.weatherforcast import WeatherForecastService


class SuccessRequest(views.APIView):
    service: WeatherForecastService = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = WeatherForecastService()

    def get(self, request, *args, **kwargs):
        return response.Response(
            data=self.service.get,
            status=status.HTTP_200_OK,
            content_type="application/json",
        )
