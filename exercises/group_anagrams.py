'''
Anagram Groups
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

    Input: strs = ["act","pots","tops","cat","stop","hat"]

    Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:

    Input: strs = ["x"]

    Output: [["x"]]

Example 3:

    Input: strs = [""]

    Output: [[""]]

Constraints:

    * 1 <= strs.length <= 1000.
    * 0 <= strs[i].length <= 100
    * strs[i] is made up of lowercase English letters.


    =================   SOLUTION:   ================
    - using a hashmap to map in an int array fashion like
'''

def groupAnagrams(strs):
    res = {}
    for word in strs:
        key_in_dict = [0] * 26

        for char in word:
            if key_in_dict[ord(char) - ord('a')] == 0:
                key_in_dict[ord(char) - ord('a')] = 1
            else:
                key_in_dict[ord(char) - ord('a')] += 1

        if tuple(key_in_dict) not in res:
            res[tuple(key_in_dict)] = [word]
        else:
            res[tuple(key_in_dict)].append(word)

    return res.values()

strs = ["cat","rye","aye","cud","cat","old","fop","bra"]
print(groupAnagrams(strs))

stuff = [['act', 'cat'], ['pots', 'tops', 'stop'], ['tops', 'stop'], ['cat'], ['stop'], ['hat']]


# BUGGY CODE

# ["act","pots","tops","cat","stop","hat"]
#  ["cat","rye","aye","cud","cat","old","fop","bra"]
# ["ddddddddddg","dgggggggggg"]