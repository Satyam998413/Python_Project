class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    curr = head
    while curr is not None:
        next = curr.next  # Save the next node
        curr.next = prev  # Reverse the link
        prev = curr       # Move prev to the current node
        curr = next       # Move curr to the next node
    return prev  # prev will be the new head

# Helper function to print the linked list
def print_linked_list(head):
    curr = head
    while curr is not None:
        print(curr.value, end=" -> ")
        curr = curr.next
    print("None")

# Example usage:
# Creating a linked list 1 -> 2 -> 3 -> 4 -> 5 -> None
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Original linked list:")
print_linked_list(head)

# Reversing the linked list
reversed_head = reverse_linked_list(head)
print("Reversed linked list:")
print_linked_list(reversed_head)