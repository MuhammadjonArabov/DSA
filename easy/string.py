'''
13. Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
'''
from typing import List


class Solution13:
    def romanToInto(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0
        for char in s:  # Time O(n)
            current_value = roman_map[char]  # Memory O(1)
            if current_value > prev_value:
                print(current_value, 888)
                total += current_value - 2 * prev_value
            else:
                total += current_value
            prev_value = current_value
        return total


solution13 = Solution13()
print(solution13.romanToInto('IV'))
print(solution13.romanToInto('VII'))
