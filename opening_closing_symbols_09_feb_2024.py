# determine whether a given string containing parentheses, brackets, and curly braces has
# a balanced arrangement of these symbols.
# It checks if each opening symbol ((, [, or {) has a corresponding closing symbol (), ], or })

import collections

def valid_parentheses(sentence: str) -> bool:
    stack = collections.deque()
    for item in sentence:
        if len(stack) == 0:
            stack.append(item)
        elif stack[-1] == "[" and item == "]":
            stack.pop()
        elif stack[-1] == "(" and item == ")":
            stack.pop()
        elif stack[-1] == "{" and item == "}":
            stack.pop()
        else:
            stack.append(item)
    return len(stack) == 0


def main():
    print(valid_parentheses("()"))
    print(valid_parentheses("()[]{}"))
    print(valid_parentheses("[([])))))))))"))


if __name__ == '__main__':
    main()