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

"""Singleton ``_nada: nada = Nada()`` represents a failure that can
propagate down the "happy path" of a calculation. It does this by

- returning itself for arbitrary method calls
- returns itself if called as a Callable with arbitrary arguments
- interpreted as an empty container by standard Python functions
- comparisons compare as true only for non-failed results.

  - thus ``a == b`` means the results of two non-failed calculations compare as equal

Given variables ``x`` and ``y`` where

- ``x: tuple[int, int] | Nada``
- ``y: tuple[int, int] | Nada``

.. table:: ``x == y``

   +--------+--------+--------+--------+
   |   x∖y  | Nada() | (1, 2) | (0, 0) |
   +========+========+========+========+
   | Nada() | false  | false  | false  | 
   +-----------+-----+--------+--------+
   | (1, 2) | false  | true   | false  |
   +--------+--------+--------+--------+
   | (0, 0) | false  | false  | true   |
   +--------+--------+--------+--------+

Of course, ``Nada() is Nada()`` is still true.

"""

from collections.abc import Callable, Iterator
from typing import Any, ClassVar, Final, final
from .sentinel import Sentinel

__all__ = ['Nada']


@final
class Nada:
    __slots__ = ()
    _instance: 'ClassVar[Nada | None]' = None
    _hash: int = 0

    SENTINEL: ClassVar[Final[Sentinel]] = Sentinel('Nada')

    def __new__(cls) -> 'Nada':
        if cls._instance is None:
            cls._instance = super(Nada, cls).__new__(cls)
            cls._hash = hash((cls._instance, (cls._instance,)))
        return cls._instance

    def __iter__(self) -> Iterator[Any]:
        return iter(())

    def __hash__(self) -> int:
        return self._hash

    def __repr__(self) -> str:
        return 'Nada()'

    def __bool__(self) -> bool:
        return False

    def __len__(self) -> int:
        return 0

    def __add__(self, right: Any) -> 'Nada':
        return Nada()

    def __radd__(self, left: Any) -> 'Nada':
        return Nada()

    def __mul__(self, right: Any) -> 'Nada':
        return Nada()

    def __rmul__(self, left: Any) -> 'Nada':
        return Nada()

    def __eq__(self, right: Any) -> bool:
        return False

    def __ne__(self, right: Any) -> bool:
        return False

    def __ge__(self, right: Any) -> bool:
        return False

    def __gt__(self, right: Any) -> bool:
        return False

    def __le__(self, right: Any) -> bool:
        return False

    def __lt__(self, right: Any) -> bool:
        return False

    def __getitem__(self, index: int | slice) -> Any:
        return Nada()

    def __setitem__(self, index: int | slice, item: Any) -> None:
        return

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return Nada()

    def __getattr__(self, name: str) -> Callable[..., Any]:
        def method(*args: Any, **kwargs: Any) -> Any:
            return Nada()

        return method

    def nada_get[T](self, alt: T | Sentinel = SENTINEL) -> Any:
        """Get an alternate value, defaults to ``Nada()``."""
        if alt == Sentinel('Nada'):
            return Nada()
        return alt
