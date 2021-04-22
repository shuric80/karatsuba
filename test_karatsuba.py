import pytest

from karatsuba import calc_karatsuba


@pytest.mark.parametrize("a,b, expected",
                         ((10, 10, 100), (12345, 6789, 83810205),
                          (10E12, 10E4, 100E16)))
def test_karatsuba(a: int, b: int, expected: int):
    assert expected == calc_karatsuba(a, b)
