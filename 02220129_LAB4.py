#Part 1: Queue Implementation using Array
class ArrayQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity  # Default capacity
        self.queue = [None] * capacity  # Underlying array storage
        self.front = -1  # Tracks the front index
        self.rear = -1   # Tracks the rear index

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, element):
        if self.is_full():
            print("Queue is full!")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = element
        print(f"Enqueued {element} to the queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        element = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        print(f"Dequeued element: {element}")
        return element

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        print(f"Front element: {self.queue[self.front]}")
        return self.queue[self.front]

    def size(self):
        if self.is_empty():
            return 0
        if self.rear >= self.front:
            return self.rear - self.front + 1
        return self.capacity - self.front + self.rear + 1

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        if self.rear >= self.front:
            print("Display queue:", self.queue[self.front:self.rear + 1])
        else:
            print("Display queue:", self.queue[self.front:] + self.queue[:self.rear + 1])

# Example usage
queue = ArrayQueue()
print(f"Created new Queue with capacity: {queue.capacity}")
print(f"Queue is empty: {queue.is_empty()}")

queue.enqueue(10)
queue.display()
queue.enqueue(20)
queue.display()
queue.enqueue(30)
queue.display()
queue.peek()
queue.dequeue()
queue.display()
print(f"Queue size: {queue.size()}")