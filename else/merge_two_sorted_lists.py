"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list."""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# t O(n)  s O(1)
def mergeTwoLists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    dummy = ListNode()  # Create a dummy node to simplify the merge process
    current = dummy  # Initialize 'current' to point to the dummy node

    while list1 and list2:
        if list1.val < list2.val:  # Compare the values of the nodes
            current.next = list1  # Link the smaller node to 'current'
            current = list1  # Move 'current' to the node just added
            list1 = list1.next  # Advance 'list1' to its next node
        else:
            current.next = list2  # Link the smaller node to 'current'
            current = list2  # Move 'current' to the node just added
            list2 = list2.next  # Advance 'list2' to its next node

    current.next = list1 if list1 else list2  # Attach the remaining nodes

    return dummy.next  # Return the merged list starting from the first node


print(mergeTwoLists([1, 2, 4], [1, 3, 4]))
# print(mergeTwoLists([], []))
# print(mergeTwoLists([], [0]))
