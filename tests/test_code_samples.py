import unittest
from src.main import analyze_code

class TestComplexityAnalyzer(unittest.TestCase):
    def test_single_loop(self):
        code = """
for i in range(n):
    print(i)
"""
        analyze_code(code)  # Expected: Time Complexity: O(n), Space Complexity: O(1)

    def test_nested_loops(self):
        code = """
for i in range(n):
    for j in range(n):
        print(i, j)
"""
        analyze_code(code)  # Expected: Time Complexity: O(n^2), Space Complexity: O(1)

    def test_sort(self):
        code = """
arr.sort()
"""
        analyze_code(code)  # Expected: Time Complexity: O(n log n), Space Complexity: O(n)

if __name__ == "__main__":
    unittest.main()