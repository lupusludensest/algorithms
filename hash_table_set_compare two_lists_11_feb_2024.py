# compare two lists. find intercession of elements. set. hash table

l_1 = [-9, 'Tanya', 'Banana', 'Apple', 'Car', 3.3] # bucket of buyer
l_2 = [-9, 'Tanya', 'Banana', 'Apple', 'Car', 3.3, 8.8, 'Vasya'] # warehouse

def set_compare_lists(l_1, l_2): # O(m + n) == O(n)
    l_2_set = set(l_2) # O(m) m - hash function/table
    for i in l_1: # O(n)
        if i not in l_2_set: # O(1)
            return False
    return True

print(set_compare_lists(l_1, l_2))