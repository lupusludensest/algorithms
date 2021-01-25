# В строке найти и заменить одну подстроку на другую.
# Если одинаковых подстрок несколько, заменить все.
# Строка, значение которое надо заменить и значение,
# на которое надо заменить вводятся с клавиатуры.
string = str(input("Enter the string: "))
print(f'\nYou entered: {string}.')

subStrOld = str(input("\nOld substring: "))
subStrNew = str(input("\nNew substring: "))
lenStrOld = len(subStrOld)

while string.find(subStrOld) >= 0:
    i = string.find(subStrOld)
    string = string[:i] + subStrNew + string[i+lenStrOld:]

print(f'\nEdited string: {string}')