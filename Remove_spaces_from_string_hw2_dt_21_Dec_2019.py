# Вводится ненормированная строка, у которой могут быть пробелы в начале, в конце и между словами более одного пробела.
# Привести ее к нормированному виду, т.е. удалить все пробелы в начале и конце,
# а между словами оставить только один пробел.
string = str(input(f'Enter the string: '))
i = 0
while string[i] == ' ':
    string = string[1:]
while string[len(string)-1] == ' ':
    string = string[:-1]
i = 1
while i < len(string)-1:
    if string[i] == ' ' and string[i+1] == ' ':
        string = string[:i+1] + string[i+2:]
    else:
        i += 1
print(f'The organized string is: "{string}".')