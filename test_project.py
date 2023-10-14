import pytest
from project import is_valid_url, is_valid_char, is_valid_time

# Test case for is_valid_url function
def test_is_valid_url():
    # Valid URL
    valid_url = "https://www.google.com"
    assert is_valid_url(valid_url) is True

    # Invalid URL
    invalid_url = "google.com"
    assert is_valid_url(invalid_url) is False

# Test case for is_valid_char function
def test_is_valid_char():
    # Valid characters
    valid_characters = ["m", "l"]
    for char in valid_characters:
        assert is_valid_char(char) is True

    # Invalid characters
    invalid_characters = ["y", "a", "1", ""]
    for char in invalid_characters:
        assert is_valid_char(char) is False

# Test case for is_valid_time function
def test_is_valid_time():
    # Valid time format
    valid_time = "12:30"
    assert is_valid_time(valid_time) is True

    # Invalid time format
    invalid_time = "25:70"
    assert is_valid_time(invalid_time) is False

    # Invalid input type
    invalid_input = 12345
    assert is_valid_time(invalid_input) is False

# Run the tests
if __name__ == "__main__":
    pytest.main()
