'''
14. Longest Common Prefix
- Easy
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

'''

def longestCommonPrefix(strs):
    res = ""

    for i in range(len(strs[0])):
        for string in strs:
            if i == len(string) or string[i] != strs[0][i]:
                return res
        res += strs[0][i]
    return res

print((longestCommonPrefix(["car", "can", "canon", "canvi"])))