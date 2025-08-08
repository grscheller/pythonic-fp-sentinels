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

from typing import reveal_type 
from pythonic_fp.singletons.nada import Nada

nada = Nada()

def add2(x: int) -> int:
    return x + 2

def gt42(x: int) -> bool|Nada:
    if x > 42:
        return True
    if x >= 0:
        return False
    return Nada()

class TestNada:
    def test_equality_identity(self) -> None:
        no1 = Nada()
        no2 = Nada()
        no3 = nada

        assert no1 is no1
        assert no2 is no2
        assert no3 is no2
        assert no1 is no2
        assert no2 is no1
        assert no1 is nada
        if no1 is not no2:
            assert False
        else:
            assert True

        assert not (no1 == no2)
        assert not no1 != no2
        assert not no3 != nada
        assert not (no1 <= no2)
        assert not (no1 >= no2)
        assert not (no1 < no2)
        assert not (no1 > no2)
        assert not (no2 <= no1)
        assert not (no2 >= no1)
        assert not (no2 < no1)
        assert not (no2 > no1)
        assert not (no1 == 5)
        assert not no1 != 5
        assert not (no1 <= 5)
        assert not (no1 >= 5)
        assert not (no1 < 5)
        assert not (no1 > 5)
        assert not (5 == no1)
        assert not 5 != no1
        assert not (5 <= no1)
        assert not (5 >= no1)
        assert not (5 < no1)
        assert not (5 > no1)


    def test_len(self) -> None:
        no1 = Nada()
        assert len(no1) == 0

    def test_iterate(self) -> None:
        no1 = Nada()
        no2 = Nada()
        l1 = [42]
        v: int
        for v in no1:
            l1.append(v)
        for v in no2:
            assert False
        assert len(l1) == 1

    def test_nget(self) -> None:
        no1 = Nada()
        no2 = Nada()
        assert no1.nada_get(42) == 42
        assert no2.nada_get(21) == 21
        got1 = no1.nada_get(Nada())
        got2 = no1.nada_get('forty-two')
        assert got1 is Nada()
        assert got2 == 'forty-two'
        assert no2.nada_get(13) == (10 + 3)
        assert no2.nada_get(10//7) == 10//7

    def test_equal_self(self) -> None:
        no1 = Nada()
        no1 != no1
        no1.nada_get(42) == no1.nada_get(42)
        no1.nada_get(42) != no1.nada_get(21)

    def test_map(self) -> None:
        no1 = Nada()
        no2 = no1.map(add2)
        assert no1 is no2 is Nada()

    def test_call(self) -> None:
        no1 = Nada()
        assert no1() is Nada()
        assert no1() is nada
        assert nada() is nada
        assert no1(42) is Nada()
        assert no1(a=1, b=2) is Nada()

    def test_get_set(self) -> None:
        no1 = Nada()
        no2 = Nada()

        no2[5] = 101
        assert no2 is nada
        got: int | Nada = no1[42]
        assert got is nada
        assert no1[2:7:1] is nada

        no2[11:20:2] = 1,2,3,4,5
        assert no2 is nada

        try:
            no2[11:20:2] = 1,2,3,4,5
        except ValueError:
            assert False
        else:
            assert True
        finally:
            assert no2 is nada

        try:
            no2[11:20:2] = 1,2,3,4,5,6
        except ValueError:
            assert True
        else:
            assert False
        finally:
            assert no2 is Nada()

        no2[11:20] = 1,2,3,4,5,6,7,8,9  # Failed test
        try:
            no2[11:20] = 1,2,3,4,5,6,7,8,9
        except ValueError:
            assert False
        else:
            assert True
        finally:
            assert no2 is Nada()

        got = no1.nada_get(42)
        assert got == 42

    def test_add_mul(self) -> None:
        no1 = Nada()
        no2 = Nada()
        assert 2 + 3 == 5
        assert not no2 + 99 != no1
        assert no2 + 99 is no1
        assert not 86 + no1 != no2
        assert 86 + no1 is no2
        assert not no2 * 99 != no1
        assert no2 * 99 is no1
        assert not 86 * no1 != no2
        assert 86 * no1 is no2

class TestArbitraryMethods:
    def test_arbitrary_methods(self) -> None:
        no1 = Nada()
        no2 = Nada()
        assert no1.foo(23, 12, bar='five') is nada
        assert no2.foo() is nada
        assert not (no1.foo(42).bar("Buggy", "the", "clown") == no2.baz(42))
        assert not (no1.foo(42).bar("Buggy", "the", "clown") != no2.baz(42))
        debug1 = no1.foo(42).bar("Buggy", "the", "clown")
        debug2 = no2.baz(42)
        debug1 == debug2  # THIS SHOULD FAIL!!!
        reveal_type(debug1)
        reveal_type(debug2)
        debug1 is Nada()
        debug2 is Nada()
        reveal_type(debug1)
        reveal_type(debug2)

class TestBooleanContext:
    def test_boolean(self) -> None:
        no1 = Nada()
        no2 = Nada()

        if no1:
            assert False
        elif no2:
            assert False
        else:
            assert True

