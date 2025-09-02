from datetime import timedelta
from typing import Callable, Iterable, Optional, Type, Union

import aiobreaker
from aiobreaker.listener import CircuitBreakerListener
from aiobreaker.storage import CircuitMemoryStorage, base
from aiobreaker.state import CircuitBreakerState
import pybreaker
from apps.sharedapp.singleton import Singleton

from .listeners import DBListener, LogListener


class CircuitBreaker(aiobreaker.CircuitBreaker, metaclass=Singleton):
    CIRCUIT_BREAKER_LISTENERS = [
        DBListener(),
        LogListener(),
    ]
    
    _prev_state = CircuitBreakerState.CLOSED
    
    @property
    def prev_state(self):
        return self._prev_state
    
    @aiobreaker.CircuitBreaker.state.setter
    def state(self, state_str):
        """
        Set cached state and notify listeners of newly cached state.
        """
        self._prev_state = self._state
        self._state = self._create_new_state(
            state_str, prev_state=self._state, notify=True)

    def __init__(
        self,
        fail_max=5,
        timeout_duration: Optional[timedelta] = None,
        exclude: Optional[Iterable[Union[Callable, Type[Exception]]]] = None,
        listeners: Optional[Iterable[CircuitBreakerListener]] = None,
        state_storage: Optional[base.CircuitBreakerStorage] = None,
        name: Optional[str] = None,
    ):
        listeners = listeners or self.CIRCUIT_BREAKER_LISTENERS
        state_storage = state_storage or CircuitMemoryStorage(
            CircuitBreakerState.OPEN,
        )
        super(CircuitBreaker, self).__init__(
            fail_max=fail_max,
            timeout_duration=timeout_duration,
            exclude=exclude,
            listeners=listeners,
            state_storage=state_storage,
            name=name,
        )
