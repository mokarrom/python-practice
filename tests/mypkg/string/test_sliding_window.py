from mypkg.string.sliding_window import (
    numKLenSubstrNoRepeats,
    count_klen_substr_no_repeat,
    lengthOfLongestSubstring,
    length_of_longest_substring,
)


def test_count_klen_substr_no_repeat():
    s = "havefunonleetcode"
    k = 5
    assert count_klen_substr_no_repeat(s, k) == 6
    assert numKLenSubstrNoRepeats(s, k) == 6

    s = "codeeveryday"
    k = 4
    assert count_klen_substr_no_repeat(s, k) == 4
    assert numKLenSubstrNoRepeats(s, k) == 4

    s = "home"
    k = 5
    assert count_klen_substr_no_repeat(s, k) == 0
    assert numKLenSubstrNoRepeats(s, k) == 0


def test_lengthOfLongestSubstring():
    s = "abcabcbb"
    assert lengthOfLongestSubstring(s) == 3
    assert length_of_longest_substring(s) == 3

    s = "bbbbb"
    assert lengthOfLongestSubstring(s) == 1
    assert length_of_longest_substring(s) == 1

    s = "pwwkew"
    assert lengthOfLongestSubstring(s) == 3
    assert length_of_longest_substring(s) == 3
