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

"""Singleton classes representing sentinel values.

Intended for library code, not to be exported/shared between modules,
otherwise some of its intended typing guarantees may be lost.

Useful substitute for ``None`` as a hidden implementation detail.

- allows ``None`` to be stored in data structures
- allows end users to choose to use ``None`` or ``()`` as "sentinel" values
- always equals itself (unlike ``NoValue``)
- never equals anything else

**Usage:**

.. code:: python

    from pythonic_fp.singletons.sentinel import Sentinel

    _my_sentinel: Final[Sentinel] = Sentinel('my_sentinel')
    _another_one: Final[Sentinel] = Sentinel('foofoo rules')

    if some_ref is _my_sentinel:
        ...

    if if some_ref is Sentinel('foofoo rules'):
        ...

.. note::

   Can be compared using either ``is`` and ``is not`` or ``==`` and ``!=``. A Sentinel
   value always equals itself and never equals anything else, especially other sentinel
   values defined with different strings.

.. tip::

   When comparing using ``==`` or ``!=`` put the known sentinel value first to ensure
   reference equality is used.

"""

__all__ = ['Sentinel']

from typing import final


@final
class Sentinel:

    __slots__ = ('_sentinel_name',)
    _instances: 'dict[str, Sentinel]' = {}

    def __new__(cls, sentinel_name: str) -> 'Sentinel':
        if sentinel_name not in cls._instances:
            cls._instances[sentinel_name] = super(Sentinel, cls).__new__(cls)
        return cls._instances[sentinel_name]

    def __init__(self, sentinel_name: str) -> None:
        self._sentinel_name = sentinel_name

    def __repr__(self) -> str:
        return "Sentinel('" + self._sentinel_name + "')"
