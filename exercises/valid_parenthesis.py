'''
20. Valid Parentheses

Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
def isValid(s):
    stack = []
    
    if( (s[0] == ')' or s[0] == ']' or s[0] == '}')) or len(s) == 1:
        return False

    stack.append(s[0])

    b = False

    i = 1

    while i < len(s):
        if len(stack) > 0:  # Check if stack is not empty
            top = stack[-1]
        else:
            top = ""

        if(top + s[i] == '()' or top + s[i] == '[]' or top + s[i] == '{}'):
            stack.pop()
        else:
            stack.append(s[i])
        i += 1

    if len(stack) == 0:
        return True
    else:
        return False

print(isValid("{[()]}"))