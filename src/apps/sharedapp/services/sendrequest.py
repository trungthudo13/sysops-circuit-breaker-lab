import aiohttp
from apps.circuit_breaker.models import CircuitBreaker
from aiobreaker.state import CircuitBreakerState
from apps.sharedapp.infras.httpclients import HttpClient
from abc import ABC, abstractmethod

from apps.sharedapp.singleton import SingletonABC


class CircuitBreakerError(Exception): ...


class SendRequestService(ABC, metaclass=SingletonABC):
    _domain_name: str = None

    def __init__(self, domain_name: str, *args, **kwargs):
        self._domain_name = domain_name
        self._breaker = CircuitBreaker()

    @abstractmethod
    def send_api(self): ...

    async def send(self, nocb=False):
        http_client = HttpClient()

        async def _do():
            async with aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(1)
            ) as session:
                return await http_client.fetch_data(
                    session=session, url=self.send_api()
                )

        try:
            # return await _do()
            return await (_do() if nocb else self._breaker.call_async(_do))
        except Exception as ex:
            if CircuitBreakerState.OPEN != self._breaker.prev_state.state:
                self._breaker.state = CircuitBreakerState.OPEN
                raise ex
            elif CircuitBreakerState.OPEN == self._breaker.state.state:
                raise CircuitBreakerError(ex)
            raise ex
