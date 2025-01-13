class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(lst):
    # Handle the case of an empty list
    if not lst:
        return None

    # Create the head of the linked list
    head = Node(lst[0])
    current = head

    # Iterate through the list and create subsequent nodes
    for value in lst[1:]:
        current.next = Node(value)
        current = current.next

    return head


def display_linked_list(lst):
    current = lst
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


head = Node(4)
nodeB = Node(2)
nodeC = Node(3)
nodeD = Node(10)

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD


def countNodes(head: Node) -> int:
    counter = 1
    current = head
    while current:
        current = current.next
        counter += 1
    return counter


# def countNodes(head, count=1):
#     if head.next != None:
#         return countNodes(head.next, count + 1)
#     return count

print(countNodes(head))
