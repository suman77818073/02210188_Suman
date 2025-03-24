class ArrayStack:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._stack = []
        self._top = -1 
        print(f"Created new ArrayStack with capacity: {self._capacity}")

    def push(self, element):
        if len(self._stack) < self._capacity:
            self._stack.append(element)
            self._top += 1
            print(f"Pushed {element} to the stack")
        else:
            print("Stack overflow: Cannot push, stack is full")
    
    def pop(self):
        if not self.is_empty():
            popped_element = self._stack.pop()
            self._top -= 1
            print(f"Popped element: {popped_element}")
            return popped_element
        else:
            print("Stack underflow: Cannot pop, stack is empty")
            return None
    
    def peek(self):
        if not self.is_empty():
            print(f"Top element: {self._stack[self._top]}")
            return self._stack[self._top]
        else:
            print("Stack is empty: No top element")
            return None
    
    def is_empty(self):
        return len(self._stack) == 0
    
    def size(self):
        return len(self._stack)
    
    def display(self):
        print(f"Display stack: {self._stack}")


stack = ArrayStack()
print("Stack is empty:", stack.is_empty())
stack.push(10)
stack.display()
stack.push(20)
stack.display()
stack.push(30)
stack.display()
stack.peek()
stack.pop()
print("Stack size:", stack.size())
stack.display()
