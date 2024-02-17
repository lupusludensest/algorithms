# compare two lists. find intercession of elements

l_1 = [-9, 'Tanya', 'Banana', 'Apple', 'Car', 3.3] # bucket of buyer
l_2 = [-9, 'Tanya', 'Banana', 'Apple', 'Car', 3.3, 8.8, 'Vasya'] # warehouse

def intercession_elmnts(l_1, l_2): # O(n * m)
    for i in l_1: # O(n) n - length of the list
        if i not in l_2: # O(m)  m - length of the list
            return False
    return True

print(intercession_elmnts(l_1, l_2))