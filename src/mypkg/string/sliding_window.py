"""This module contains all sliding window or two pointer related problems."""
from typing import Dict


def lengthOfLongestSubstring(s: str) -> int:
    """Find the length of the longest substring without repeating characters.

    Time complexity: O(n)
    Space complexity: O(m), where m is the size of set, and it is bounded by min(n, number_of_chars).
    Ref: https://leetcode.com/problems/longest-substring-without-repeating-characters/
    """
    length, left, right = 0, 0, 0
    seen: Dict[str, int] = dict()  # <char, position>
    while right < len(s):
        if s[right] in seen:  # when we see a duplicate, we can jump left pointer to the 'right + 1' position.
            left = max(left, seen[s[right]] + 1)

        seen[s[right]] = right
        length = max(length, right - left + 1)
        right += 1

    return length


def length_of_longest_substring(s: str) -> int:
    """Find the length of the longest substring without repeating characters.

    Time complexity: O(2n) = O(n)
    Space complexity: O(m), where m is the size of set, and it is bounded by min(n, number_of_chars).
    Ref: https://leetcode.com/problems/longest-substring-without-repeating-characters/
    """
    left = length = 0
    seen = set()  # set of unique chars in the current window.
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        length = max(length, right - left + 1)

    return length


def count_klen_substr_no_repeat(s: str, k: int) -> int:
    """Return the number of substrings in s of length k with no repeated characters."""
    # https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/
    n = len(s)
    if n < k or k > 26:
        return 0

    left, substr_count = 0, 0
    distinct_chars = set()  # contains distinct chars in current window
    for right in range(n):
        # if current char is already in the current window, remove all chars up to the current char (inclusive)
        while s[right] in distinct_chars:
            distinct_chars.remove(s[left])
            left += 1

        # Add current char into the current window, i.e., distinct chars set.
        distinct_chars.add(s[right])

        if right - left + 1 == k:  # Check if the length of current window is k
            substr_count += 1
            distinct_chars.remove(s[left])  # contract the window by removing the left most char.
            left += 1

    return substr_count
