class node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def makeLL(LL):
    head = node(LL[0], None)
    current = head
    for i in range(1, len(LL)):
        newNode = node(LL[i], None)
        current.next = newNode
        current = current.next
    return head


def printLL(LL):
    current = LL
    while current:
        print(current.val, end=' ')
        current = current.next


def reverseLL(head):
    def reverse_helper(node):
        # Base case: if the node is null or the last node, return it
        if not node or not node.next:
            return node

        # Reverse the rest of the list recursively
        new_head = reverse_helper(node.next)

        # Update the next pointers to reverse the link
        node.next.next = node
        node.next = None

        # Return the new head of the reversed list
        return new_head

    # Call the helper function starting from the head
    return reverse_helper(head)


# Create a sample linked list
newLL = makeLL([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Print the original list
print("Original list:")
printLL(newLL)

# Reverse the list and print the reversed list
reversed_list = reverseLL(newLL)
print("\nReversed list:")
printLL(reversed_list)
