# PayPay Corp invited you to take PayPay Corp - QA Coding Challenge on CodeSignal

# Write a function returning a sum of digits of integer "n" which has two digits
# def solution(n):
#     str_n = str(n)
#     str_a = str_n[0]
#     str_b = str_n[1]
#     if not (0 <= int(str_a) <= 9 and 0 <= int(str_b) <= 9):
#         raise ValueError("Both nums must be single digits")
#
#     return int(str_a) + int(str_b)
#
# print(solution(21))

# Quiz. What is the next number in the following sequence?
# 1, 1, 2, 3, 5, 8, 13, *
# A: 21

# What happens when user asks the browser
# A:
# 1. URL parsing;
# 2. DNS lookup;
# 3. Request heats loadbalancer of the site;
# 4. HTTP/S request procesed by the web server;
# 5. Responce (200 if success) and data transfer (HTML returned to the browser);
# 6. Page rendering in the browser;
# 7. JavaScript execution;
# 8. Page displayed in the browser;
# 9. User interacts with a dynamic page and JavaScript updates the page;

# Real challenge 21 nov 2023

# 1 code challenge
# Codewritting
# Solve the code challenge:
# You are developing a new programming language and currently working on variable names.
# You have a list of words that you consider to be good and could be used for variable names.
# All the strings in words consist of lowercase English letters.
# A complex variable name is a combination (possibly with repetitions) of some strings from words,
# written in CamelCase. In other words, all the strings are written without spaces and each string
# (with the possible exception of the first one) starts with a capital letter.
# Your programming language should accept complex variable names only.
# You need to check if the variableName is accepted by your programming language.
# Example
# For words = ["is", "valid", "right"] and variableName = "isValid", the output should be solution
# (words, variableName) = true.
# As variableName consists of words "is" and "valid", and both of them are in words.
# For words = ["is", "valid", "right"] and variableName = "IsValid", the output should be solution
# (words, variableName) = true.
# Note that both variants: "IsValid" and "isValid" are valid in CamelCase.
# For words = ["is", "valid", "right"] and variableName = "isValId", the output should be solution
# (words, variableName) = false.
# variableName is separated to words "is", "val", "id", and not all words are in words.

import re
def solution(words, variableName):
    parts = re.findall('[A-Z][^A-Z]*', variableName)

    for part in parts:
        if part.lower() not in words:
            return False

    return True

print(solution(["is", "valid", "right"], "isValid"))
print(solution(["is", "valid", "right"], "isValId"))


def solution(words, variableName):
    parts = []
    current_word = ''

    for char in variableName:
        if char.islower():
            current_word += char
        else:
            if current_word:
                parts.append(current_word)
            current_word = char

    if current_word:
        parts.append(current_word)

    for part in parts:
        if part.lower() not in words:
            return False

    return True

print(solution(["is", "valid", "right"], "isValid"))
print(solution(["is", "valid", "right"], "isValId"))

# 2 code challenge
# Codewriting
# You are given the prices of a stock, in the form of an array of integers, prices.
# Let's say that prices[i] is the price of the stock on the ith day (0-based index). Assuming that you are allowed
# to buy and sell the stock only once, your task is to find the maximum possible profit (the difference between the buy and sell prices).
# Note: You can assume there are no fees associated with buying or selling the stock.
# Example
# For prices = [6, 3, 1, 2, 5, 4], the output should be solution(prices) = 4.
# It would be most profitable to buy the stock on day 2 and sell it on day 4. Thus, the maximum
# profit is prices[4] - prices[2] = 5 - 1 = 4.
# For prices = [8, 5, 3, 1], the output should be solution(prices) = 0.
# Since the value of the stock drops each day, there's no way to make a profit from selling it.
# Hence, the maximum profit is 0.
# For prices = [3, 100, 1, 97], the output should be solution(prices) = 97.
# It would be most profitable to buy the stock on day 0 and sell it on day 1. Thus, the maximum
# profit is prices[1] - prices[0] = 100 - 3 = 97.

def solution(prices):
    mn = prices[0]
    mx_dff = 0

    for i in range(1, len(prices)):
        mn = min(mn, prices[i])
        mx_dff = max(mx_dff, prices[i] - mn)

    return mx_dff

print(solution([6, 3, 1, 2, 5, 4]))
print(solution([1, 3, 1, 2, 6, 4]))




