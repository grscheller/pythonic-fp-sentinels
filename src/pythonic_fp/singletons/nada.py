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
- in comparisons compare as true only for non-failed results.

  - thus ``a == b`` means the results of two non-failed calculations compare as equal
  - thus ``a != b`` means the results of two non-failed calculations compare as not equal

- hashable

Given variables ``x`` and ``y`` where

- ``x: tuple[int, int] | Nada``
- ``y: tuple[int, int] | Nada``

.. table:: ``x == y``

   +--------+--------+--------+--------+
   |   x∖y  | Nada() | (1, 2) | (0, 0) |
   +========+========+========+========+
   | Nada() | Nada() | Nada() | Nada() | 
   +--------+--------+--------+--------+
   | (1, 2) | Nada() | True   | false  |
   +--------+--------+--------+--------+
   | (0, 0) | Nada() | False  | true   |
   +--------+--------+--------+--------+

Where the ``Nada()`` singleton is "falsy".

Of course, ``Nada() is Nada()`` is always true, so we can always
identify a failed calculation.

.. code:: python

    def f(n: int) -> int | Nada:
        ...

    result = f(0)*f(0) + 12  # contrived calculation that can fail
    if result >= 42:
       final_result: int = 42
    else:
       final_result = result.nada_get(0)

.. warning::

    Non-standard (un-pythonic) comparison operators.

.. warning::

    Threadsafe only if instantiated before going multi-threaded.

"""

from collections.abc import Callable, Iterable, Iterator
from typing import Any, ClassVar, final

__all__ = ['Nada']


@final
class Nada:
    __slots__ = ()
    _instance: 'ClassVar[Nada | None]' = None
    _hash: ClassVar[int] = 0

    def __new__(cls) -> 'Nada':
        if cls._instance is None:
            cls._instance = super(Nada, cls).__new__(cls)
            cls._hash = hash((cls._instance, (cls._instance,)))
        return cls._instance

    def __iter__(self) -> Iterator[Any]:
        return iter(())

    def __repr__(self) -> str:
        return 'Nada()'

    def __hash__(self) -> int:
        return self._hash

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

    def __eq__(self, right: Any) -> 'Nada':
        return Nada()

    def __ne__(self, right: Any) -> 'Nada':
        return Nada()

    def __ge__(self, right: Any) -> 'Nada':
        return Nada()

    def __gt__(self, right: Any) -> 'Nada':
        return Nada()

    def __le__(self, right: Any) -> 'Nada':
        return Nada()

    def __lt__(self, right: Any) -> 'Nada':
        return Nada()

    def __delitem__(self, index: int | slice) -> 'Nada':
        return Nada()

    def __getitem__(self, index: int | slice) -> 'Nada':
        return Nada()

    # have not considered negative indexed slices yet
    # have not considered empty iterables yet either
    def __setitem__(self, index: int | slice, items: Any) -> None:
        if items is Nada():
            return Nada()

        if isinstance(index, slice):
            if isinstance(items, Iterable):
                start = 0 if index.start is None else index.start
                step = 1 if index.step is None else index.step
                stop = index.stop
                if stop is None:
                    return Nada()
                else:
                    size_slice = (stop - start + 1) // step

                if hasattr(items, '__len__'):
                    len_iter = len(items)
                else:
                    len_iter = 0
                    for _ in items:
                        len_iter += 1

                if size_slice == len_iter:
                    return Nada()
                msg = f'attempt to assign sequence of size {len_iter} to extended slice of size {size_slice}'
                raise ValueError(msg)
            else:
                msg = 'must assign iterable to extended slice'
                raise TypeError(msg)
        return Nada()
            
    def __call__(self, *args: Any, **kwargs: Any) -> 'Nada':
        return Nada()

    def __getattr__(self, name: str) -> Callable[..., 'Nada']:
        def method(*args: Any, **kwargs: Any) -> 'Nada':
            return Nada()

        return method

    def nada_get[T](self, alt: T) -> T:
        """Get an alternate value, must only be called on ``Nada()`` itself."""
        return alt
