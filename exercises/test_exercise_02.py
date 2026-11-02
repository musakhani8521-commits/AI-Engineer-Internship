
from exercise_02 import even_or_odd

def test_even():
    assert even_or_odd(10) == "Even"

def test_odd():
    assert even_or_odd(7) == "Odd"

def test_zero():
    assert even_or_odd(0) == "Even"
