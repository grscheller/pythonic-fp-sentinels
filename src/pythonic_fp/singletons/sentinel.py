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

Can be used with functions,

.. code:: python

    from pythonic_fp.singletons.sentinel import Sentinel

    _my_sentinel: Final[Sentinel[str]] = Sentinel('my_sentinel')
    ultimate_one: Final[Sentinel[int]] = Sentinel(42)
    one_sentinel: Final[Sentinel[int]] = Sentinel(1)

    def figure_something_out(n: int, x: float) -> Sentinel[int]
        ...

    def do_something(sentinel: Sentinel[int]):
        ...

    do_something(figure_something_out(0, 1.5))

Or with classes,

.. code:: python

    class my_class:
        def __init__(self, value: float | Sentinel[str]) -> None:
            if value is _my_sentinel:
                self.value = 42.0
            else:
                self.value = value

        def get_value(self) -> float:
            return self.value

.. note::

   Can be compared using ``is``, ``is not``, ``==``, ``!=``. A Sentinel
   value always equals itself and never equals anything else, especially
   other sentinel values defined with different flavors.

.. tip::

   Useful substitute for ``None`` for "optional" values. Don't export to
   use as a hidden implementation detail. Does not clash with end user
   code which may use either ``None`` or ``()`` as "sentinel" values.

   To ensure that reference equality is used for either ``==`` or ``!=``,
   put the known sentinel value first.

"""
from typing import final, Hashable, TypeVar

__all__ = ['Sentinel']

H = TypeVar("H", bound=Hashable)

@final
class Sentinel[H]:

    __slots__ = ('_flavor',)

    _instances: 'dict[H, Sentinel[H]]' = {}

    def __new__(cls, flavor: H) -> 'Sentinel[H]':
        if flavor not in cls._instances:
            cls._instances[flavor] = super(Sentinel[H], cls).__new__(cls)
        return cls._instances[flavor]

    def __init__(self, flavor: str) -> None:
        self._flavor = flavor

    def __repr__(self) -> str:
        return "Sentinel('" + self._flavor + "')"
