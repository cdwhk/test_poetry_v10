from test_poetry_v10.palindrome import is_palindrome

def test_is_palindrome():
    assert is_palindrome("radar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("level") == True
    assert is_palindrome("") == True  # Edge case: empty string
