from project import view_count
import pytest

def main():
    test_invalid()
    test_valid()

def test_invalid():
    assert view_count("Ten") == "That's not a valid number. Please try again."

def test_valid():
    assert view_count(1000) == "1000"


if __name__ == "__main__":
    main()