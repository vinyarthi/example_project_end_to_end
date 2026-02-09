import pytest # pyright: ignore[reportMissingImports] 
from src.core.calculator import add,multiply,divide,subtract

def test_add():
    assert add(2,3) == 5

def test_multiply():
    assert multiply(12,4) == 48

def test_divide():
    assert divide(4,2) == 2

def test_subtract():
    assert subtract(10,14) == -4

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)


