class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None
        self.size_counter = 0
        print("Created new LinkedStack")

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node
        self.size_counter += 1
        print(f"Pushed {element} to the stack")
        self.display()

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop element.")
            return None
        popped_element = self.top.data
        self.top = self.top.next
        self.size_counter -= 1
        print(f"Popped element: {popped_element}")
        self.display()
        return popped_element

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Cannot peek.")
            return None
        print(f"Top element: {self.top.data}")
        return self.top.data

    def is_empty(self):
        return self.size_counter == 0

    def size(self):
        return self.size_counter

    def display(self):
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Display stack:", elements)

# Example usage
if __name__ == "__main__":
    linked_stack = LinkedStack()
    print(f"Stack is empty: {linked_stack.is_empty()}")
    
    linked_stack.push(10)
    linked_stack.push(20)
    linked_stack.push(30)
    
    linked_stack.peek()
    print(f"Stack size: {linked_stack.size()}")
    
    linked_stack.pop()
    
    # Format for the final stack display
    current = linked_stack.top
    formatted_stack = []
    while current:
        formatted_stack.append(current.data)
        current = current.next
    print("Current stack:", " -> ".join(map(str, formatted_stack)) + " -> null")
    
    print(f"Stack size: {linked_stack.size()}")