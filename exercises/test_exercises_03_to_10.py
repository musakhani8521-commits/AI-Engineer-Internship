
from exercise_03 import find_max
from exercise_04 import factorial
from exercise_05 import reverse_string
from exercise_06 import count_vowels
from exercise_07 import remove_duplicates
from exercise_08 import is_prime
from exercise_09 import calculate_average
from exercise_10 import count_words

def test_maximum():
    assert find_max([10, 20, 5]) == 20

def test_factorial():
    assert factorial(5) == 120

def test_reverse():
    assert reverse_string("Python") == "nohtyP"

def test_vowels():
    assert count_vowels("hello") == 2

def test_duplicates():
    assert remove_duplicates([1, 2, 2, 3]) == [1, 2, 3]

def test_prime():
    assert is_prime(7) is True
    assert is_prime(8) is False

def test_average():
    assert calculate_average([10, 20, 30]) == 20

def test_word_count():
    assert count_words("I love Python") == 3
