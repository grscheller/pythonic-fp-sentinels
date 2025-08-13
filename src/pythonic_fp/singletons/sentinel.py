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

"""Sentinel values of different flavors.

Can be used with functions or classes,

.. code:: python

    from typing import Final
    from pythonic_fp.singletons.sentinel import Sentinel

    my_sentinel: Final[Sentinel[str]] = Sentinel('my_sentinel')
    ultimate_one: Final[Sentinel[int]] = Sentinel(42)
    one_sentinel: Final[Sentinel[int]] = Sentinel(1)

    def figure_something_out(n: int, x: float) -> Sentinel[int]
        ...

    def do_something(sentinel: Sentinel[int]):
        ...

    do_something(figure_something_out(0, 1.5))

    class my_class:
        def __init__(self, value: float | Sentinel[str]) -> None:
            if value is my_sentinel:
                self.value = 42.0
            else:
                self.value = value

        def get_value(self) -> float:
            return self.value

Can be used as a private implementation detail for a class,

.. code:: python

    __all__ = ['my_class']

    from typing import ClassVar, Final, final
    from pythonic_fp.singletons.sentinel import Sentinel

    @final
    class my_class():

        _sentinel: Final[ClassVar[Sentinel[str]]] = Sentinel('_my_class_secret_str')

        def __init__(self, number: int | Sentinel[str] = self._sentinel) -> None:
            if number is _sentinel:
                self.number = 42
            else:
                self.number = number

        def get_number(self) -> int:
            return self.number

.. note::

   Threadsafe.

.. note::

   Can be compared using ``==`` and ``!=``. A Sentinel
   value always equals itself and never equals anything else,
   especially other sentinel values defined with different flavors.

.. tip::

   Useful substitute for ``None`` for "optional" values. Don't export to
   use as a hidden implementation detail. Does not clash with end user
   code which may use either ``None`` or ``()`` as "sentinel" values.

   To ensure that reference equality is used for either ``==`` or ``!=``,
   put the known sentinel value first.

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
