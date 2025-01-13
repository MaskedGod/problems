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


a1 = list_to_linked_list([1, 8])
b1 = list_to_linked_list([0])
# a1 = list_to_linked_list([2, 4, 3])
# b1 = list_to_linked_list([5, 6, 4])
# a1 = ListNode(2)
# a2 = ListNode(4)
# a3 = ListNode(3)
# a1.next = a2
# a2.next = a3

# b1 = ListNode(5)
# b2 = ListNode(6)
# b3 = ListNode(4)
# b1.next = b2
# b2.next = b3


def count_nodes(head: ListNode) -> int:
    counter = 0
    current = head
    while current:
        counter += 1
        current = current.next
    return counter


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy_head = ListNode(0)
    tail = dummy_head
    carry = 0

    while l1 or l2 or carry != 0:
        digit1 = l1.val if l1 else 0
        digit2 = l2.val if l2 else 0

        nodes_sum = digit1 + digit2 + carry
        digit = nodes_sum % 10
        carry = nodes_sum // 10

        tail.next = ListNode(digit)
        tail = tail.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy_head.next


print(display_linked_list(add_two_numbers(a1, b1)))

# def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
#    carry = 0
#     l3 = ListNode()
#     dummy = l3
#     while l1 or l2 or carry:
#         if l1:
#             carry+=l1.val
#             l1 = l1.next
#         if l2:
#             carry += l2.val
#             l2 = l2.next
#         digit, carry = carry%10, carry//10
#         l3.next = ListNode(digit)
#         l3 = l3.next
#     return dummy.next
