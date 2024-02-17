# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false

s1 = "({}{}[({})])"
s2 = "(){()}{}[{}((){"
s3 = "({}[(())[[[[][({})])"
s4 = "(){}[])"
s5 = "([{}]())"

# def is_balanced(s): # stack solution
#     res = []
#     for i in s:
#         res.append(i)
#         if len(res) > 1 and res[-2:] in [['(', ')'], ['{', '}'], ['[', ']']]:
#             res.pop()
#             res.pop()
#     return not res
#
# print(str(is_balanced(s1)))  #True
# print(str(is_balanced(s2)))  #False
# print(str(is_balanced(s3)))  #False
# print(str(is_balanced(s4)))  #False
# print(str(is_balanced(s5)))  #True

def is_balanced_1(s):
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')
    return not s

print(str(is_balanced_1(s1)))  #True
print(str(is_balanced_1(s2)))  #False
print(str(is_balanced_1(s3)))  #False
print(str(is_balanced_1(s4)))  #False
print(str(is_balanced_1(s5)))  #True


