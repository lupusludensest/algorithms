print(f'1')
input = 'aaaabbbccdddd'
# expected output is: output = '4a3b2c4d'
def cntltrs(input):
 output = ''
 for n in range(0, len(input)):
    if (len(output) == 0 or input[n] != output[-1]):
     if input.count(input[n]) > 0 and input[n - 1] == input[n]:
        output += (str(input.count(input[n - 1])) + input[n - 1])
 return f'{output}'
print(cntltrs(input))


print(f'\n2')
from collections import defaultdict
def run_me(string):
    
    hash_table = defaultdict(int)

    for char in string:
        hash_table[char] += 1

    res = ''

    for k, v in hash_table.items():
        res += f'{v}{k}'
        
    return res
output = run_me('aaaabbbccdddd')
print(output)  # '4a3b2c4d'


print(f'\n3')
from collections import Counter
input = 'aaaabbbccddddaaaa'
output = ''

for k, v in Counter(input).items():
    output += f'{v}{k}'
print(output)  # '4a3b2c4d'

print(f'\n4-exactly what is required')
input = 'aaaabbbccddddaaaa'
output = ''
count = 0
cur_char = ''

for char in input:
    if char == cur_char:
        count += 1
        continue

    else:
        output += f'{count}{cur_char}' if count > 0 else ''
        cur_char = char
        count = 1
else:
    output += f'{count}{cur_char}'     
print(output)  # '4a3b2c4d'


print(f'\n5')
input = 'aaaabbbccddddaaaa'
def run_me(input):
    
    hash_table = {} # empty dictionary declared

    for char in input: # iterate every char in the string input
        if char in hash_table: # if element char is in dictionary-which is false in the first iterarion
            hash_table[char] +=1 # if element char is in dictionary-add 1 to its value in dictionary

        else:
            hash_table[char] = 1 # if element char is not in dictionary-it accepts 1
         
    res = '' # empty string is declared

    for k, v in hash_table.items(): # for every pair of key and value in dictionary
        res += f'{v}{k}' # empty string accepts pairs of values and keys
        
    return res
output = run_me(input)
print(output)  # '4a3b2c4d'

print(f'\n6')
input = 'aaaabbbccdddd'
def some_func(input):
    char_dict = {}
    for i in input:
        if i not in char_dict:
            char_dict[i] = 1
        else:
            if list(char_dict)[-1] == i:
                char_dict[i] += 1
    return ''. join([k+str(v) for k, v in char_dict.items()])
print(some_func(input))

