class Node:
    def __init__(self, data=None):
        self.data = data  # stores the data element
        self.next = None  # references the next node
class LinkedQueue:
    def __init__(self):
        self.front = None  # points to the front of the queue
        self.rear = None   # points to the rear of the queue
        self.size = 0      # tracks the number of elements

    def is_empty(self):
        return self.size == 0

    def enqueue(self, element):
        new_node = Node(element)
        if self.rear:  # If the queue is not empty, add to the rear
            self.rear.next = new_node
        self.rear = new_node
        if self.front is None:  # If the queue was empty, the new node is the front as well
            self.front = new_node
        self.size += 1
        print(f"Enqueued {element} to the queue")
        self.display()

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue")
            return None
        dequeued_data = self.front.data
        self.front = self.front.next
        if self.front is None:  # If the queue is now empty, set rear to None
            self.rear = None
        self.size -= 1
        print(f"Dequeued element: {dequeued_data}")
        self.display()
        return dequeued_data

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        print(f"Front element: {self.front.data}")
        return self.front.data

    def size(self):
        return self.size

    def display(self):
        current = self.front
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(f"Display queue: {elements}")
queue = LinkedQueue()
print(f"Created new LinkedQueue")
print(f"Queue is empty: {queue.is_empty()}")
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.peek()
queue.dequeue()
print(f"Queue size: {queue.size}")
