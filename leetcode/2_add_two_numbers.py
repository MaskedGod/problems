"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(lst):
    # Handle the case of an empty list
    if not lst:
        return None

    # Create the head of the linked list
    head = ListNode(lst[0])
    current = head

    # Iterate through the list and create subsequent nodes
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def display_linked_list(lst):
    current = lst
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


a1 = list_to_linked_list([2, 4, 3])
b1 = list_to_linked_list([5, 6, 4])


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    pass


print(addTwoNumbers(a1, b1))
# Traverse and print the linked list to verify
