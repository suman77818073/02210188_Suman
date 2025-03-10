class CustomList:
    def __init__(self, capacity=10):
        self._capacity = capacity  
        self._size = 0             
        self._elements = [None] * self._capacity  

    def add(self, item):
        if self._size >= self._capacity:
            self._resize()
        self._elements[self._size] = item
        self._size += 1

    def _resize(self):
        new_capacity = self._capacity * 2
        new_elements = [None] * new_capacity
        for i in range(self._size):
            new_elements[i] = self._elements[i]
        self._elements = new_elements
        self._capacity = new_capacity

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        return self._elements[index]

    def size(self):
        return self._size

    def capacity(self):
        return self._capacity

custom_list = CustomList()
custom_list.add(1)
custom_list.add(2)
print(custom_list.get(0))  
print(custom_list.size())   
print(custom_list.capacity()) 