import heapq

def find_max(w, array):
    start = 0
    hip = []
    ans = []
    while start+w <= len(array):
        hip = array[start:start+w]
        heapq._heapify_max(hip)
        ans.append(hip[0])
        start += 1

    return ans

arr = [-4, 2, -5, 3, 6]

answer = find_max(3, arr)
print(answer)

class Heap():
    def __init__(self):
        self.heap = [0]
        self.current_size = 0 # helps with integer division

    def bubble_up(self, i):
        while i // 2 > 0:
            if self.heap[i] > self.heap[i // 2]:
                tmp = self.heap[i // 2]
                self.heap[1 // 2] = self.heap[i]
                self.heap[i] = tmp

            i = i // 2

    def heap_push(self, k):
        self.heap.append(k)
        self.currentSize = self.currentSize + 1
        self.bubble_up(self.current_size)

    def bubble_down(self, i):
        while (i*2) <= self.current_size:
            mc = self.max_child(i):
            if self.heap[i] < self.heap[mc]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[mc]
                self.heap[mc] = tmp

            i = mc

    def max_child(self, i):
        if i*2 + 1 > self.currentSize:
            return i * 2

        if self.heap[i*2] > self.heap[i*2 + 1]:
            return i*2
        else:
            return i*2 + 1

    def heap_pop(self):
        ret_val = self.heap[1]
        self.heap[1] = self.heap[self.current_size]
        self.current_size = self.current_size - 1
        self.heap.pop()
        self.bubble_down(1)
        return ret_val

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heap = [0] + alist[:]
        while (i > 0):
            self.bubble_down(i)
            i = i - 1