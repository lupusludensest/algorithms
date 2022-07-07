# Print a string in reverse order

# 1. Using loop
# string = str(input('Enter the string: '))
# def reverse(string):
#   str = ''
#   for i in string:
#     str = i + str
#   return str
#
# print ("The original string  is : ",end="")
# print (string)
# print ("The reversed string(using loops) is : ",end="")
# print (reverse(string))

# 2. Using recursion
# string = str(input('Enter the string: '))
# def reverse(string):
#     if len(string) == 0:
#         return string
#     else:
#         return reverse(string[1:]) + string[0]
# print("The original string  is : ", end="")
# print(string)
# print("The reversed string(using recursion) is : ", end="")
# print(reverse(string))

# 3. Using stack
# Function to create an empty stack. It initializes size of stack as 0
# def createStack():
#     stack = []
#     return stack
#
# # Function to determine the size of the stack
# def size(stack):
#     return len(stack)
#
# # Stack is empty if the size is 0
# def isEmpty(stack):
#     if size(stack) == 0:
#         return true
#
# # Function to add an item to stack. It increases size by 1
# def push(stack, item):
#     stack.append(item)
#
# # Function to remove an item from stack. It decreases size by 1
# def pop(stack):
#     if isEmpty(stack): return
#     return stack.pop()
#
# # A stack based function to reverse a string
# def reverse(string):
#     n = len(string)
#
#     # Create a empty stack
#     stack = createStack()
#
#     # Push all characters of string to stack
#     for i in range(0, n, 1):
#         push(stack, string[i])
#
# # Making the string empty since all characters are saved in stack
#     string = ""
#
# # Pop all characters of string and put them back to string
#     for i in range(0, n, 1):
#         string += pop(stack)
#
#     return string
#
# # Driver code
# string = str(input('Enter the string: '))
# print ("The original string  is : ",end="")
# print (string)
# print ("The reversed string(using stack) is : ",end="")
# print (reverse(string))

# 4. Using extended slice syntax
# Python code to reverse a string using extended slice syntax

# Function to reverse a string
# def reverse(string):
#     string = string[::-1]
#     return string
#
# string = str(input('Enter the string: '))
#
# print("The original string  is : ", end="")
# print(string)
# print("The reversed string(using extended slice syntax) is : ", end="")
# print(reverse(string))

# 5. Using reversed
# Python code to reverse a string
# using reversed()

# # Function to reverse a string
# def reverse(string):
#     string = "".join(reversed(string))
#     return string
#
# string = str(input('Enter the string: '))
#
# print("The original string  is : ", end="")
# print(string)
# print("The reversed string(using reversed) is : ", end="")
# print(reverse(string))

# print("This is the rat,\nThat ate the malt\nThat lay in the house that Jack built")

# num = 456
# first_digit = num // 100
# # print(first_digit)
# middle_digit = (num // 10) % 10
# # print(middle_digit)
# last_digit = num % 10
# # print(last_digit)
# s = first_digit + middle_digit + last_digit
# # print(s)

lst=[]
a=round(float(input(f'Enter value to number "a" : ')), 2)
lst.append(a)
b=round(float(input(f'Enter value to number "b" : ')), 2)
lst.append(b)
c=round(float(input(f'Enter value to number "c" : ')), 2)
lst.append(c)
print(f'Lst: "{lst}"')

s=round(sum(lst), 2)
print(f'Sum of "{a}", "{b}", "{c}" as a members of list "{lst}" is "{s}".')
