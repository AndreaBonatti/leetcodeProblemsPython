# Problem 206.
# Reverse Linked List.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        string = "["
        current_node = self
        while current_node is not None:
            if current_node != self:
                string += ","
            string += str(current_node.val)
            current_node = current_node.next
        string += "]"
        return string


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node = None
        current_node = head

        while current_node is not None:
            forward_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = forward_node
            # e.g [1, 2, 3, 4, 5]
            # forward_node = 1.next = 2
            # current_node.next = previous_node = None
            # previous_node = current_node = 1
            # current_node = forward_node = 2

        return previous_node


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Input: " + str(head))
    print("Output: " + str(Solution().reverseList(head)))
