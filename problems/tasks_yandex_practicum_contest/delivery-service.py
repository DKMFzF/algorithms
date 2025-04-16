from typing import List

"""
17 апр 2025, 04:07:22
136868973
A
Python 3.12.3
OK
-
64ms
4.64Mb
-	-
отчёт
"""


def min_platforms(weights: List[int], limit: int) -> int:
    weights.sort()
    left, right = 0, len(weights) - 1
    platforms = 0

    while left <= right:
        if weights[left] + weights[right] <= limit:
            left += 1
        right -= 1
        platforms += 1

    return platforms


if __name__ == "__main__":
    robots = list(map(int, input().split()))
    max_weight = int(input())
    print(min_platforms(robots, max_weight))
