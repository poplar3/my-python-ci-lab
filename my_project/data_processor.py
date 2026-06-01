# Обработка списка данных

from typing import List, Union, Optional


def filter_even_numbers(numbers: List[int]) -> List[int]:
    return [n for n in numbers if n % 2 == 0]


def calculate_average(numbers: List[Union[int, float]]) -> Optional[float]:
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def find_maximum(numbers: List[Union[int, float]]) -> Optional[Union[int, float]]:
    if not numbers:
        return None
    return max(numbers)
