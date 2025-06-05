import heapq

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __repr__(self):
        return f"({self.value}, {self.priority})"

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def peek(self):
        if self.elements:
            return self.elements[0][1]
        return None

    def insert(self, value, priority):
        node = Node(value, priority)

        heapq.heappush(self.elements, (-node.priority, node))

    def remove(self):
        if self.elements:
            return heapq.heappop(self.elements)[1]
        return None

    def __repr__(self):
        return str([node for priority, node in sorted(self.elements)])


pq = PriorityQueue()

pq.insert("t1", 3)
pq.insert("t2", 1)
pq.insert("t3", 2)

print(pq)

print(pq.remove())

print(pq.peek())
