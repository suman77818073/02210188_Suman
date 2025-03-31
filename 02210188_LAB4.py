class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        print("Created new LinkedQueue")
    
    def is_empty(self):
        return self.size == 0
    
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        print(f"Enqueued {element} to the queue")
        self.display()
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        print(f"Dequeued element: {removed_data}")
        self.display()
        return removed_data
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.front.data
    
    def get_size(self):
        return self.size
    
    def display(self): 
        if self.is_empty():
            print("Display queue: []")
        else:
            current = self.front
            queue_str = " -> ".join(str(current.data) for current in self.iterate()) + " -> null"
            print(f"Current queue: {queue_str}")
    
    def iterate(self):
        current = self.front
        while current:
            yield current
            current = current.next

# Example Usage:
queue = LinkedQueue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Front element:", queue.peek())
dequeued_element = queue.dequeue()
print("Queue size:", queue.get_size())
