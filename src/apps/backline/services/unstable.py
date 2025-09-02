import os
import random
import time

from apps.backline.services.weatherforcast import WeatherForecastService
from apps.sharedapp.singleton import Singleton


class UnstableException(Exception):
    pass


class UnstableService(metaclass=Singleton):
    fail_rate = float(os.getenv("FAIL_RATE", "0.7"))
    slow_rate = float(os.getenv("SLOW_RATE", "0.7"))
    sleep_s = float(os.getenv("SLEEP", "1.0"))

    __service = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__service = WeatherForecastService()

    @property
    def get(self):
        if random.random() < self.slow_rate:
            time.sleep(self.sleep_s)

        if random.random() < self.fail_rate:
            raise UnstableException({"error": "downstream failed"})

        return self.__service
