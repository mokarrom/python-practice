from mypkg.string.sliding_window import (
    numKLenSubstrNoRepeats,
    count_klen_substr_no_repeat,
    lengthOfLongestSubstring,
    length_of_longest_substring,
    minWindow,
    lengthOfLongestSubstringTwoDistinct,
    lengthOfLongestSubstringTwoDistinct_2,
    lengthOfLongestSubstringKDistinct,
    numberOfSubstrings,
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


def test_minWindow():
    s = "ADOBECODEBANC"
    t = "ABC"
    assert minWindow(s, t) == "BANC"

    s = "a"
    t = "a"
    assert minWindow(s, t) == "a"

    s = "a"
    t = "aa"
    assert minWindow(s, t) == ""

    s = "ab"
    t = "a"
    assert minWindow(s, t) == "a"


def test_lengthOfLongestSubstringTwoDistinct():
    s = "eceba"
    assert lengthOfLongestSubstringTwoDistinct(s) == 3
    assert lengthOfLongestSubstringTwoDistinct_2(s) == 3

    s = "ccaabbb"
    assert lengthOfLongestSubstringTwoDistinct(s) == 5
    assert lengthOfLongestSubstringTwoDistinct_2(s) == 5

    s = "abaccc"
    assert lengthOfLongestSubstringTwoDistinct(s) == 4
    assert lengthOfLongestSubstringTwoDistinct_2(s) == 4


def test_lengthOfLongestSubstringKDistinct():
    s = "eceba"
    k = 2
    assert lengthOfLongestSubstringKDistinct(s, k) == 3

    s = "aa"
    k = 1
    assert lengthOfLongestSubstringKDistinct(s, k) == 2


def test_numberOfSubstrings():
    s = "abcabc"
    assert numberOfSubstrings(s) == 10

    s = "aaacb"
    assert numberOfSubstrings(s) == 3

    s = "abc"
    assert numberOfSubstrings(s) == 1
