from my_project.data_processor import (
    filter_even_numbers,
    calculate_average,
    find_maximum,
)


class TestDataProcessor:
    def test_filter_even_numbers(self):
        assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
        assert filter_even_numbers([1, 3, 5]) == []
        assert filter_even_numbers([]) == []

    def test_calculate_average(self):
        assert calculate_average([1, 2, 3, 4, 5]) == 3.0
        assert calculate_average([10, 20, 30]) == 20.0
        assert calculate_average([]) is None
        assert calculate_average([5]) == 5.0

    def test_find_maximum(self):
        assert find_maximum([3, 7, 2, 9, 1]) == 9
        assert find_maximum([-5, -1, -10]) == -1
        assert find_maximum([]) is None
