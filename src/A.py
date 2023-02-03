from typing import Dict, Tuple, List, TypeVar, Generic, Callable


class BeObserved(object):
    T = TypeVar('T')

    def __init__(self, value: Generic[T], callback: Callable | None = None) -> None:
        self._value = value
        self._observers = []
        if callback != None:
            self._observers.append(callback)

    @property
    def value(self) -> T:
        return self._value

    @value.setter
    def value(self, value: T):
        self._value = value
        for callback in self._observers:
            callback(self._value)

    def bind(self, callback: Callable[[T], T]):
        self._observers.append(callback)


a = BeObserved(value=12,)