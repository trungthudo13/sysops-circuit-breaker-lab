from functools import cache
import logging
from aiobreaker.listener import CircuitBreakerListener


class DBListener(CircuitBreakerListener):
    "Listener used by circuit breakers that execute database operations."

    def before_call(self, cb, func, *args, **kwargs):
        "Called before the circuit breaker `cb` calls `func`."

    def state_change(self, cb, old_state, new_state):
        "Called when the circuit breaker `cb` state changes."

    def failure(self, cb, exc):
        "Called when a function invocation raises a system error."
        # cache.get("")
        # return exc

    def success(self, cb):
        "Called when a function invocation succeeds."

class LogListener(CircuitBreakerListener):
    "Listener used to log circuit breaker events."

    def state_change(self, cb, old_state, new_state):
        msg = "State Change: CB: {0}, New State: {1}".format(cb.name, new_state)
        logging.info(msg)