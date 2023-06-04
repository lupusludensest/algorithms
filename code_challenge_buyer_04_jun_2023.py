# # find min amd maxi in the list
# lst_1 = [-10099, -4, 0, 4, 6, 88]
# min_i = max_i = lst_1[0]
# for i in lst_1:
#     if i < min_i:
#         min_i = i
#     if i > max_i:
#         max_i = i
# print(min_i, max_i)

# bayer test 04 jun 2023, sunday
# Question 4/4
#
# "Bank Account Program"
#
# Your solution will be scored against multiple hidden test cases, with a sample case being provided for your reference.
#
# The default code includes a mechanism for reading input strings. You will need to parse these strings into the appropriate variables as needed.
#
# The output data type is not a concern, as long as the characters within the output box match the expected outcome.
#
#
# Time limit: 90 minutes
#
#
# Write a simple bank program which has the following rules:
#
#     • Two bank account types: checking and savings.
#     • Accounts have a balance.
#     • Three transaction types: deposit, withdraw, and transfer.
#     • Checking accounts have a withdrawal limit of 500 per transaction.
#     • Savings account has a withdrawal limit of 300 per transaction.
#     • Units only use integers, no decimals (e.g. 20, not 20.00)
#
# Create the following functions:
#
# Function 1: `initialize` - It initializes the bank account with params provided by the input.
# Eg: If the input is "new 0 100", the function should initialize a bank account with a checking balance of 0 and a savings balance of 100. It should print "0 100" (without quotes) to indicate the balance of the corresponding account. Please print in this order: checking savings. Separate each value with a space.
#
# Function 2: `deposit` - It adds money into the bank account, based on provided by the input.
# Eg: If the input is "deposit 500 checking", it should deposit 500 to the checking account and print out a balance of "500 100" (without quotes) based on function 1.
#
# Function 3: `withdraw` - It withdraws money from the bank account, based on params from the input.
# Eg: If the input is "withdraw 200 checking", it should print out a balance of “300 100" (without quotes) based on functions 1 and 2.
# Note: Due to the withdrawal limit, if the attempt is over the limit, the transaction must be cancelled. It should NOT change the balance.
# If a checking withdrawal amount is larger than the checking account balance, it should deduct the checking account balance first and then deduct the rest from savings account. However, if it's a savings withdrawal and the amount is larger than the savings account balance, the transaction must simply be cancelled and it should NOT change the balance.
#
# Function 4: `transfer` - It transfers money between checking and savings, based on params from the input.
# Eg: If the input is "transfer 300 checking", it should transfer 300 from the checking account to the savings account.
# Note: If the transfer amount is larger than the balance, the transaction must simply be cancelled and it should NOT change the balance.
#
# Input explanation:
# Input consists of multiple lines. Each line of input is a function name followed by a space and param(s) to be used in the function.
# Function 1 will always be placed at the first line, and will be called only once.
#
# Output explanation:
# It should print the bank account balance per each transaction, and separate them by a line break.
# Code evaluation is based on your output, please follow the sample format and do NOT print anything else.
#
#
#
# new 0 100
# deposit 500 checking
# withdraw 600 checking
# withdraw 200 checking
# transfer 301 checking
# deposit 100 savings
# withdraw 100 checking
# withdraw 500 savings
# withdraw 400 checking
# Sample Input
# 0 100
# 500 100
# 500 100
# 300 100
# 300 100
# 300 200
# 200 200
# 200 200
# 0 0

# # Use urllib.request to send network request if needed.

# import fileinput

# inputData = ''

# for line in fileinput.input():
#     inputData += line


# def code_here():
#     # Use the function to return the solution.
#     return inputData


# print(code_here())

def initialize(checking_init, savings_init):
    checking = savings = 0
    checking += checking_init
    savings += savings_init
    return f'{checking} {savings}'
print(initialize(0, 100))

def deposit(dpst, to_where):
    checking = 0
    savings = 100
    to_where = to_where.lower()
    if to_where == 'checking':
        checking += dpst
        return f'{checking} {savings}'
    elif to_where == 'savings':
        savings += dpst
        return f'{checking} {savings}'
print(deposit(500, 'checking'))

def withdraw(wtdr, fr_where):
    checking = 500
    savings = 100
    if wtdr > 500 and fr_where == 'checking':
        return f'enter valid amount no more $500'
    elif wtdr > 300 and fr_where == 'savings':
        return f'enter valid amount no more $300'
    else:
        if wtdr <= 500 and wtdr <= checking and fr_where == 'checking':
            checking = checking - wtdr
            return f'withdraw {checking} checking'
        elif wtdr <= 500 and wtdr <= savings and fr_where == 'savings':
            savings = savings - wtdr
            return 'withdraw {checking} savings'
print(withdraw(600, 'checking'))

def transfer(trns, fr_where, to_where):
        checking = 999
        savings = 9999
        if trns <= savings and fr_where == 'savings' and to_where == 'checking':
            checking = checking + trns
            return f'checking: ${checking}, savings: ${savings}'
        elif trns <= checking and fr_where == 'checking' and to_where == 'savings':
            savings = savings + trns
            return f'checking: {checking}, savings: {savings}'
print(transfer(555, f'savings', 'checking'))
























