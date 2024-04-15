'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Input: head = [1,2]
Output: [2,1]
1->2->3->4
linked list = many nodes that linked together
1[next 2]->2[next 7]->7[next 10]->10[next NONE]
'''


class node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def makeLL(LL):
    head = node(LL[0], None)
    current = head
    for i in range(1, len(LL)):
        newNode = node(LL[i], None)
        current.next = newNode #1->
        current = current.next
    return head


def printLL(LL):
    current = LL
    while current:
        print(current.val, end=' ')
        current = current.next


def reverseLL(LL):
    prev, current = None, LL
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


newLL = makeLL([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
printLL(newLL)
print(" ")
printLL(reverseLL(newLL))
print(" ")
print(type(newLL))