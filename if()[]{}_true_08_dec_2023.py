# Given string by user. "()[]{}". If "(]", if "([)]" false.

a = input('Enter the string: ')
def check_brackets(a):
    bopen = ['(', '[', '{']
    bclose = [')', ']', '}']
    stack = []

    for char in a:
        if char in bopen:
            stack.append(char)
        elif char in bclose:
            pos = bclose.index(char)
            if ((len(stack) > 0) and (bopen[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False

print(check_brackets(a))

# s = input("Enter the word: ")
# def isValid(s):
#     stack = []
#     for char in s:
#         if char in ['(', '[', '{']:
#             stack.append(char)
#         elif char == ')':
#             if not stack or stack[-1] != '(':
#                 return False
#             stack.pop()
#         elif char == ']':
#             if not stack or stack[-1] != '[':
#                 return False
#             stack.pop()
#         elif char == '}':
#             if not stack or stack[-1] != '{':
#                 return False
#             stack.pop()
#
#     return not stack
#
# print(isValid(s))
