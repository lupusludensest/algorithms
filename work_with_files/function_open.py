# work with the files in Python

# file = open(r'E:\Gurov_SSD_256\IT\Testing\Automation_08_09_2019\\algorithms\work_with_files\\file.txt', encoding='utf-8')
# file = open('file.txt', 'r', encoding='utf-8')
# file = open('file.txt', 'w', encoding='utf-8')
# print(file.read())
# print(file.read(3))
# print(file.read(3))
# file.seek(0)
# print(file.read(3))
# print(file.readline())
# print(file.readline())

# for row in file:
#     print(row, end='')

# for row in file:
#     for letter in row:
#         print(letter)
# lst_1 = file.readlines()
# print(lst_1)

# file = open('file.txt', 'w', encoding='utf-8')
# file.write('Hello world!\n')
# file.write('How are you?\n')
# file = open('file.txt', 'r', encoding='utf-8')
# print(file.read())

# file = open('file.txt', 'a', encoding='utf-8')
# file.write('Hello world!\n')
# file.write('How are you?\n')
# file = open('file.txt', 'r', encoding='utf-8')
# print(file.read())

file = open('file.txt', 'a+', encoding='utf-8')
file.write('Hello world!\n')
file.write('How are you?\n')
file = open('file.txt', 'r', encoding='utf-8')
print(file.read())

file.close() # close the file to prevent leaks
