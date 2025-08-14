# Copyright 2023-2025 Geoffrey R. Scheller
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Sentinel values of different flavors. Can be used
with functions or classes.

**Some Use Casses**

Could be used like an Enum.

.. code:: python

    from pythonic_fp.singletons.sentinel import Sentinel

    def calculate_something(n: int, x: float) -> tuple[Sentinel[int], float]:
        if n <= 0:
            return (Sentinel(0), x)
        return (Sentinel(n), x/n)

    def process_result(pair: tuple[Sentinel[int], float]) -> float:
        if pair[0] is Sentinel(0):
            return 0.0
        return pair[1]

    result = process_result(calculate_something(213, 15234.541))

Can be also be used as a private implementation detail for a class.
Here is an example of an class that can take an "optional" value
yet still be able to store ``None`` as a value.

.. code:: python

    from typing import ClassVar, Final
    from pythonic_fp.singletons.sentinel import Sentinel

    class my_class:

        _sentinel: Final[ClassVar[Sentinel[str]]] = Sentinel('_my_class_secret_str')

        def __init__(self, value: float | None | Sentinel[str]) -> None:
            if value is my_sentinel:
                self.value = 42.0
            else:
                self.value = value

        def get_value(self) -> float | None:
            return self.value

.. note::

   Threadsafe.

.. note::

   Can be compared using ``==`` and ``!=``. A Sentinel
   value always equals itself and never equals anything else,
   especially other sentinel values.

   To ensure that reference equality is used put the known
   sentinel value first.

.. tip::

   - don't export when using as a hidden implementation detail.
   - does not clash with end user code

     - which may use ``None`` or ``()`` as their "sentinel" values.


"""
import threading
from typing import ClassVar, final, Hashable, TypeVar

__all__ = ['Sentinel']

H = TypeVar("H", bound=Hashable)

@final
class Sentinel[H]:

    __slots__ = ('_flavor',)

    _flavors: 'dict[H, Sentinel[H]]' = {}
    _lock: ClassVar[threading.Lock] = threading.Lock()

    def __new__(cls, flavor: H) -> 'Sentinel[H]':
        if flavor not in cls._flavors:
            with cls._lock:
                if flavor not in cls._flavors:
                    cls._flavors[flavor] = super(Sentinel, cls).__new__(cls)
        return cls._flavors[flavor]

    def __init__(self, flavor: H) -> None:
        if not hasattr(self, '_flavor'):
            self._flavor = flavor

    def __repr__(self) -> str:
        return "Sentinel('" + repr(self._flavor) + "')"
