import ctypes


class DynamicArray(object):
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    # Return number of elements sorted in array
    def __len__(self):
        return self.n

    # Return element at index k
    def __getitem__(self, index):
        if index <= 0 or index > n:
            return IndexError("Index is out of bounds!")

        return self.A[k]

    def get_capacity(self):
        return self.capacity

    # Add element to end of the array
    def append(self, item):
        if self.n == self.capacity:
            self._resize(self.capacity * 2)

        self.A[self.n] = item
        self.n += 1

    # Resize internal array to capacity new_cap
    def _resize(self, new_capacity):
        B = self.make_array(new_capacity)

        for i in range(self.n):
            B[i] = self.A[i]

        self.A = B
        self.capacity = new_capacity
        del B

    # Returns a new array with new_cap capacity
    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()


arr = DynamicArray()
print(f'Length: {len(arr)};  Capacity: {arr.get_capacity()}')

arr.append(1)
arr.append(1)
arr.append(1)
arr.append(1)
arr.append(1)

print(f'Length: {len(arr)};  Capacity: {arr.get_capacity()}')