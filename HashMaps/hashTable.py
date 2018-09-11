class HashTable(object):
    def __init__(self, capacity, load):
        self.capacity = capacity
        self.load = load
        self.cur_capacity = 0

        self.slots = [[] for _ in range(self.capacity)]

    def set(self, key, value):
        self.slots[get(key)].append(value)

    def get(self, key):
        return key % self.capacity
