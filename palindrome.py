class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

def is_palindrome(head):
    values = []
    current = head
    while current:
        values.append(current.data)     
        current = current.next
   
    return values == values[::-1]


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

if is_palindrome(head):
    print("The linked list is a palindrome")
else:
    print("The linked list is NOT a palindrome")