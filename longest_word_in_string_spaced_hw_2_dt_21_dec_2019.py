# В строке, состоящей из слов, разделенных пробелом, найти самое длинное слово. Слово вводится с клавиатуры.
string = str(input("Enter the strings: "))
length = len(string)
m = 0
index = 0
count = 0
for i in range(length):
    if string[i] != ' ':
        count += 1
    else:
        if count > m:
            m = count
            index = i - count
        count = 0

if count > m:
    m = count
    index = i - count + 1

print(f'The longest word is: "{string[index:index + m]}", length: "{len(string[index:index + m])}".')

def lnfs_wrd_str_max(string):
    return f'The longest word is: "{max(list(string.split()), key=len)}", length: "{len(max(list(string.split()), key=len))}"'

print(lnfs_wrd_str_max(string))

def lnfs_wrd_str_sort(string):
    lst = list(string.split())
    lst.sort(key=len)
    return f'The longest word is: "{max(list(string.split()), key=len)}", length: "{len(max(list(string.split()), key=len))}"'

print(lnfs_wrd_str_sort(string))


# find the longest word in the string
s = str(input('Enter the phrase: '))
def lng_wr(s):
    lng_wr = ''
    for i in s.split():
        if len(i) > len(lng_wr):
            lng_wr = i

    return lng_wr

print(lng_wr(s))


