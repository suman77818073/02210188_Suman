class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None  
        self.tail = None 
        self._size = 0    
        print("Created new LinkedList")
        print(f"Current size: {self._size}")
        print(f"Head: {self.head}")

    def append(self, element):
        new_node = Node(element)  
        if not self.head: 
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node 
            self.tail = new_node       
        self._size += 1
        print(f"Appended {element} to the list")

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
        new_node.next = self.head 
        self.head = new_node        
        if not self.tail:          
            self.tail = new_node
        self._size += 1
        print(f"Prepended {element} to the list")

    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Print Linked list:", elements)


linked_list = LinkedList()
linked_list.append(5)         
linked_list.get(0)            
linked_list.set(0, 10)         
print(f"Current size: {linked_list.size()}")  
linked_list.prepend(10)       
linked_list.append(5)          
linked_list.print_list()      