# Работа со строками

def reverse_string(s: str) -> str:
    return s[::-1]

def count_vowels(s: str) -> int:
    vowels = set('aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ')
    return sum(1 for char in s if char in vowels)

def is_palindrome(s: str) -> bool:
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]
