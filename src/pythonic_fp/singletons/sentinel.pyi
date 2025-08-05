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

__all__ = ['Sentinel']

from typing import final

@final
class Sentinel:
    __slots__ = ('_sentinel_name',)

    _instances: dict[str, Sentinel]

    def __init__(self, sentinel_name: str) -> None: ...
    def __new__(cls, sentinel_name: str) -> Sentinel: ...
    def __repr__(self) -> str: ...
