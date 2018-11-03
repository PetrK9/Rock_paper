from fz import fizzbuzz
import pytest


def test_takes_number_str():
    assert isinstance(fizzbuzz(1), str)

@pytest.mark.parametrize(('number', 'expected'), 
                            [(1, '1'),
                             (2, '2'),
                             (4, '4'),
                             (7, '7'),
                             (11, '11')])
def test_regular_returns_numbers(number, expected):
    result = fizzbuzz(number)
    assert int(result) == number


@pytest.mark.parametrize('number', [3, 6, 9, 12])
def test_threes_returns_fizz(number):
    result = fizzbuzz(number)
    assert result == 'fizz'

@pytest.mark.parametrize('number', [5, 10, 25, 35])
def test_fives_returns_bazz(number):
    result = fizzbuzz(number)
    assert result == 'bazz'

@pytest.mark.parametrize('number', [5*3*10, 5*3, 5*3*3, 5*3*2])
def test_fives_and_there_returns_fizzbuzz(number):
    result = fizzbuzz(number)
    assert result == 'fizzbuzz'

def test_cannot_fizzbuzz_str():
    with pytest.raises(TypeError):
        fizzbuzz("nope")

def test_cannot_fizzbuzz_None():
    with pytest.raises(TypeError):
        fizzbuzz(None)

def test_cannot_fizzbuzz_fl():
    with pytest.raises(TypeError):
        fizzbuzz(5.5)



