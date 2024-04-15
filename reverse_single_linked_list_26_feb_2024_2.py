from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def list_to_array(self):
        nodes = []
        node = self
        while node is not None:
            nodes.append(node.val)
            node = node.next
        return nodes

    def __repr__(self):
        nodes = []
        node = self
        while node is not None:
            nodes.append(node.val)
            node = node.next
        return ' '.join([str(i) for i in nodes])


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        res = None
        while node is not None:
            next_node = node.next
            node.next = res
            res = node
            node = next_node
        return res


def main():
    linked_list = ListNode(10)
    linked_list = ListNode(9, linked_list)
    linked_list = ListNode(8, linked_list)
    linked_list = ListNode(7, linked_list)
    linked_list = ListNode(6, linked_list)
    linked_list = ListNode(5, linked_list)
    linked_list = ListNode(4, linked_list)
    linked_list = ListNode(3, linked_list)
    linked_list = ListNode(2, linked_list)
    linked_list = ListNode(1, linked_list)
    print(linked_list)
    res = Solution().reverseList(linked_list)
    print(res)


if __name__ == '__main__':
    main()