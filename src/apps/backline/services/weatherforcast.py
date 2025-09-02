from datetime import datetime, timedelta
from random import randint
from apps.sharedapp.singleton import Singleton


class WeatherForecastService(metaclass=Singleton):
    SUMMARIES = [
        "Freezing",
        "Bracing",
        "Chilly",
        "Cool",
        "Mild",
        "Warm",
        "Balmy",
        "Hot",
        "Sweltering",
        "Scorching",
    ]

    @property
    def get(self):
        today = datetime.now()
        return [
            {
                "date": (today + timedelta(days=idx+1)).strftime("%d/%m/%Y"),
                "temperature_c": randint(-20, 55),
                "summary": self.SUMMARIES[randint(0, len(self.SUMMARIES) - 1)],
            }
            for idx in range(5)
        ]
