# 1.Посчитайте, сколько раз символ встречается в строке. Строка и символ вводятся с клавиатуры.

#1 : Naive method
string = str(input("Enter the string: ")).lower()
symbol_to_count = str(input("Enter the symbol to count: ")).lower()

symbols_in_string = len(string)

count = 0
for i in string:
    if i == symbol_to_count:
        count = count + 1

percent_symbol = round(count/symbols_in_string*100, 2)

print(f'Symbols in the string: {symbols_in_string} total. '
      f'\nSymbol "{symbol_to_count}" repeated in the string: {count} times. '
      f'\nOr is : {percent_symbol}%.')

##########

#2 : Using count()
# test_str = str(input("Enter the string: ")).lower()
# symbol_to_count = str(input("Enter the symbol to count: ")).lower()
#
# # using count() to get count
# # counting e
# counter = test_str.count(symbol_to_count)
# length_of_string = len(test_str)
# percent_symbol = round(counter/length_of_string*100, 2)
#
# # printing result
# print(f'Symbol "{symbol_to_count}" in "{test_str}" repeated  {counter} times. '
#       f'\nLength of the string is: {length_of_string}. '
#       f'\nOr : {percent_symbol}%')

##########

#3 : Using collections.Counter()
# from collections import Counter
# string = str(input("Enter the string: ")).lower()
# symbol = str(input("Enter the symbol: ")).lower()
# length = len(string)
#
# count = Counter(string)
# percent = round(count[symbol]/length*100, 2)
# print (f'Count of "{symbol}" in "{string}" is :{count[symbol]}. '
# f'\nOr %: "{percent}"')

##########

#4 : Using lambda + sum() + map()
# test_str = str(input("Enter the string: ")).lower()
# symbol = str(input("Enter the symbol: ")).lower()
#
# count = sum(map(lambda x : 1 if symbol in x else 0, test_str))
# length = len(test_str)
# percent = round(count/length*100, 2)
# print(f'Symbol: "{symbol}" in "{test_str}" repeated "{count}" times.'
#       f'\nOr "{percent}" percent.')

#5 : Using re + findall()
# import re
# test_str = str(input("Enter the string: ")).lower()
# e = str(input("Entet the symbol: ")).lower()
#
#
# count = len(re.findall("e", test_str))
#
# print(f'Symbol "{e}" in "{test_str}" repeated "{count}" times. '
#       f'\nOr "{count/len(test_str)*100}" percent.')
