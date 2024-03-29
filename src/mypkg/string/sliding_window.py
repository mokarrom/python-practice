"""This module contains all sliding window or two pointer related problems."""
from typing import Set, Dict
from collections import defaultdict, Counter


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
    seen: Set[str] = set()  # set of unique chars in the current window.
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        length = max(length, right - left + 1)

    return length


def numKLenSubstrNoRepeats(s: str, k: int) -> int:
    """Return the number of substrings in s of length k with no repeated characters.

    Time complexity: O(n)
    """
    n = len(s)
    if n < k:
        return 0

    substr_count = 0
    dist_chars: Dict[str, int] = defaultdict(int)
    for i in range(n):
        dist_chars[s[i]] += 1
        if i > k - 2:
            if len(dist_chars) == k:
                substr_count += 1
            if dist_chars[s[i - k + 1]] > 1:
                dist_chars[s[i - k + 1]] -= 1
            else:
                del dist_chars[s[i - k + 1]]

    return substr_count


def count_klen_substr_no_repeat(s: str, k: int) -> int:
    """Return the number of substrings in s of length k with no repeated characters.

    Time complexity: O(2n) = O(n)
    Ref: https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/
    """
    n = len(s)
    if n < k or k > 26:
        return 0

    left, substr_count = 0, 0
    distinct_chars: Set[str] = set()  # contains distinct chars in the current window
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


def minWindow(s: str, t: str) -> str:
    """Return the minimum window substring of s such that all character in t is included in the window.

    Time Complexity: O(|S| + |T|)
    Space Complexity: O(|S| + |T|)
    Ref: https://leetcode.com/problems/minimum-window-substring/
    """
    t_counter = Counter(t)
    w_counter: Dict[str, int] = {}  # this is a frequency counter (<char, frequency>) of the current window.
    start = min_start = count = 0
    min_len = len(s) + 1  # the length of a substring cannot be greater than the length of string itself.

    for end in range(len(s)):
        ch = s[end]

        if ch not in t_counter:
            continue

        w_counter[ch] = w_counter.get(ch, 0) + 1

        if w_counter[ch] == t_counter[ch]:
            count += 1

        # Contract the window to get a smaller one until the window is valid.
        while count == len(t_counter):
            if end - start + 1 < min_len:
                min_len = end - start + 1
                min_start = start

            ch = s[start]
            start += 1
            if ch not in t_counter:
                continue
            w_counter[ch] -= 1
            if w_counter[ch] < t_counter[ch]:
                count -= 1

    return "" if min_len == len(s) + 1 else s[min_start : min_start + min_len]


def lengthOfLongestSubstringTwoDistinct(s: "str") -> "int":
    """Return the length of the longest substring that contains at most two distinct characters.

    Time complexity: O(2n) = O(n)
    Space complexity: O(1)
    Ref: https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
    """
    dist_counter: Dict[str, int] = dict()
    left = length = 0

    for right in range(len(s)):
        ch = s[right]
        dist_counter[ch] = dist_counter.get(ch, 0) + 1

        # contract window until it gets valid
        while len(dist_counter) > 2:
            ch = s[left]
            if dist_counter[ch] > 1:
                dist_counter[ch] -= 1
            else:
                del dist_counter[ch]
            left += 1

        # update max length
        length = max(length, right - left + 1)

    return length


def lengthOfLongestSubstringTwoDistinct_2(s: "str") -> "int":
    """Return the length of the longest substring that contains at most two distinct characters.

    Time complexity: O(n)
    Space complexity: O(1)
    Ref: https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
    """
    n = len(s)
    if n < 3:
        return n

    # sliding window left and right pointers
    left, right = 0, 0

    dist_chars_map = dict()
    max_len = 2

    for right in range(n):
        # expand the window
        dist_chars_map[s[right]] = right

        if len(dist_chars_map) == 3:
            # delete the leftmost character
            del_idx = min(dist_chars_map.values())
            del dist_chars_map[s[del_idx]]

            # contract the slide window by moving left pointer.
            left = del_idx + 1

        # update max_len
        max_len = max(max_len, right - left + 1)

    return max_len


def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    """Return the length of the longest substring of s that contains at most k distinct characters.

    Ref: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
    """
    n = len(s)
    if n < k:
        return n

    max_len = left = 0
    dist_chars_map = {}

    for right in range(n):
        dist_chars_map[s[right]] = right

        if len(dist_chars_map) == k + 1:
            del_idx = min(dist_chars_map.values())
            del dist_chars_map[s[del_idx]]
            left = del_idx + 1

        max_len = max(max_len, right - left + 1)

    return max_len


def numberOfSubstrings(s: str) -> int:
    """Given a string s consisting only of characters a, b and c.

    Return the number of substrings containing at least one occurrence of all these characters a, b and c.
    Ref: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

    Explanation:  input = "abcabc" output = 10
    ------------

    abc = 1       "abc"
    a bca = 2     "bca", "abca"
    ab cab = 3    "cab", "bcab", "abcab"
    abc abc = 4   "abc", "cabc", "bcabc", "abcabc"
    """
    map = {}
    count = 0
    for i in range(len(s)):
        map[s[i]] = i
        if len(map) == 3:
            count += min(map.values()) + 1  # count all left substrings
    return count
