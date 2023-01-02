# using list as a stack

my_lst = ['Pay bills', 'Tidy up', 'Walk the dog', 'Buy groceries', 'Cook dinner', 'Do homework', 'Go to bed']
stack = []
for task in my_lst:
    stack.append(task)
while stack:
    print(stack.pop(), ' - Done!')
print(f'\nThe stack is empty!')