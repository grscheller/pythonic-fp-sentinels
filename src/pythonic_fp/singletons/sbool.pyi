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

from typing import Final, Never

__all__ = ['SBool', 'Truth', 'Lie', 'TRUTH', 'LIE']

class SBool(int):
    def __new__(cls) -> SBool: ...
    def __repr__(self) -> str: ...
    def flavor(self) -> str | Never: ...

class Truth(SBool):
    _instances: dict[str, Truth]

    def __new__(cls, flavor: str = 'DEFAULT_TRUTH') -> Truth: ...
    def __init__(self, flavor: str = 'DEFAULT_TRUTH') -> None: ...
    def __repr__(self) -> str: ...
    def flavor(self) -> str: ...

class Lie(SBool):
    _instances: dict[str, Lie]

    def __new__(cls, flavor: str = '') -> Lie: ...
    def __init__(self, flavor: str = '') -> None: ...
    def __repr__(self) -> str: ...
    def flavor(self) -> str: ...

TRUTH: Final[Truth]
LIE: Final[Lie]

def snot(val: SBool) -> SBool: ...
