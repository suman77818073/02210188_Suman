class ArrayStack:
    def __init__(self, capacity=10):
        self._data, self._top, self._capacity = [None] * capacity, -1, capacity
        print(f"Created new ArrayStack with capacity: {capacity}")
    
    def __str__(self):
        return str(self._data[:self._top + 1])
    
    def is_empty(self):
        return self._top == -1
    
    def push(self, item):
        if self._top + 1 == self._capacity:
            self._resize(2 * self._capacity)
        self._top += 1
        self._data[self._top] = item
        print(f"Pushed {item} to the stack")
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        item, self._data[self._top] = self._data[self._top], None
        self._top -= 1
        print(f"Popped element: {item}")
        return item
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        print(f"Top element: {self._data[self._top]}")
        return self._data[self._top]
    
    def size(self):
        print(f"Stack size: {self._top + 1}")
        return self._top + 1
    
    def display(self):
        print(f"Display stack: {self._data[:self._top + 1]}")
    
    def _resize(self, new_capacity):
        self._data, self._capacity = self._data + [None] * (new_capacity - self._capacity), new_capacity

# Example Output
test_stack = ArrayStack()
print("Stack is empty:", test_stack.is_empty())
test_stack.push(10)
test_stack.display()
test_stack.push(20)
test_stack.display()
test_stack.push(30)
test_stack.display()
test_stack.peek()
test_stack.pop()
test_stack.size()
test_stack.display()
