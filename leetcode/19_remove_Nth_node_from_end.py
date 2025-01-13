# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(lst):
    if not lst:
        return None

    head = ListNode(lst[0])
    current = head

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


# get length of list and subtract nth from length. go through list with counter and in place change next node at the right place
# Could you do this in one pass?
# list with nodes. get nth-1 element from end from list and make next nth+1
def remove_nth_from_ends(head: ListNode, n: int) -> ListNode:
    # O(n)
    nodes_list = []

    while head:
        nodes_list.append(head)
        head = head.next

    list_length = len(nodes_list)

    if n == list_length:
        return nodes_list[1] if list_length > 1 else None

    prev_node = nodes_list[list_length - (n + 1)]
    prev_node.next = prev_node.next.next

    return nodes_list[0]


head = list_to_linked_list([1, 2, 3, 4, 5])
print(display_linked_list(remove_nth_from_ends(head, 2)))
