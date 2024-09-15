'''
Is Anagram

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

    Input: s = "racecar", t = "carrace"

    Output: true

Example 2:

    Input: s = "jar", t = "jam"

    Output: false

Constraints:

- s and t consist of lowercase English letters.

'''

def isAnagram(s, t):
    new_s = {}
    for char in s:
        if char not in new_s:
            new_s[char] = 1
        else:
            new_s[char] += 1

    new_t = {}
    for char in t:
        if char not in new_t:
            new_t[char] = 1
        else:
            new_t[char] += 1

    if new_s == new_t:
        return True
    return False

print(isAnagram('racecar', 'carrace'))