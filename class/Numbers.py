class Numbers(object):
    def __init__(self):
        self.data = []

    def insert(self,num):
        self.data.append(num)

    def get(self, idx):
        if idx >= len(self.data):
            return None
        else:
            return self.data[idx]

numbers = Numbers()
numbers.insert(1)
numbers.insert(2)
print(numbers.get(0))
print(numbers.get(1))
print(numbers.get(2))
numbers.insert(3)
print(numbers.get(2))
