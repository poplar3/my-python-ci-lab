from my_project.string_utils import reverse_string, count_vowels, is_palindrome


class TestStringUtils:
    def test_reverse_string(self):
        assert reverse_string("hello") == "olleh"
        assert reverse_string("Python") == "nohtyP"
        assert reverse_string("") == ""
    
    def test_count_vowels(self):
        assert count_vowels("hello") == 2
        assert count_vowels("Python") == 1
        assert count_vowels("AEIOU") == 5
        assert count_vowels("bcdfg") == 0
    
    def test_is_palindrome(self):
        assert is_palindrome("A man, a plan, a canal: Panama") == True
        assert is_palindrome("race a car") == False
        assert is_palindrome("") == True
