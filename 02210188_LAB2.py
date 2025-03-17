class Node:
    def __init__(self, data):
        self.data = data  # Data field to store the element
        self.next = None  # Next field to reference the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Head reference to the first node
        self.tail = None  # Tail reference to the last node
        self._size = 0    # Size counter to track the number of elements
        print("Created new LinkedList")
        print(f"Current size: {self._size}")
        print(f"Head: {self.head}")

    def append(self, element):
        new_node = Node(element)  # Create a new node
        if not self.head:  # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Link the old tail to the new node
            self.tail = new_node        # Update the tail to the new node
        self._size += 1
        print(f"Appended {element} to the list")
        print(f"Current size: {self._size}")

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        print(f"Element at index {index}: {current.data}")
        return current.data

    def set(self, index, element):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = element
        print(f"Set element at index {index} to {element}")
        print(f"Element at index {index}: {current.data}")

    def size(self):
        return self._size

    def prepend(self, element):
        new_node = Node(element)
        new_node.next = self.head  # Link the new node to the old head
        self.head = new_node        # Update the head to the new node
        if not self.tail:           # If the list was empty
            self.tail = new_node
        self._size += 1
        print(f"Prepended {element} to the list")
        print(f"Current size: {self._size}")

    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Print Linked list:", elements)

# Example usage
linked_list = LinkedList()
linked_list.append(5)          # List: [5]
linked_list.get(0)             # Output: Element at index 0: 5
linked_list.set(0, 10)         # List: [10]
linked_list.get(0)             # Output: Element at index 0: 10
linked_list.prepend(10)        # List: [10, 10]
linked_list.append(5)          # List: [10, 10, 5]
linked_list.print_list()       # Output: Print Linked list: [10, 10, 5]