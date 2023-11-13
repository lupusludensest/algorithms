# an example function in Python to compute the parity of a word:
wrd = str(input('Enter the word: '))

def prty_f_wrd(wrd):
    cnt = 0
    for i in wrd:
        cnt += 1

    if cnt % 2 == 0:
        return f'even'
    return f'odd'

print(prty_f_wrd(wrd))