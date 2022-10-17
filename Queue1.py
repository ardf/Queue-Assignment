class Queue:
    def __init__(self, n=10):
        self.data = []
        self.count = 0
        self.size = n

    def is_Full(self):
        return self.count == self.size

    def is_Empty(self):
        return self.count == 0

    def enQueue(self, element):
        if self.is_Full():
            print("Queue is Full")
            return
        else:
            self.data.append(element)
            self.count += 1
            print("Inserted Successfully")
            return

    def deQueue(self):
        if self.is_Empty():
            print("Queue is Empty")
            return
        else:
            print("Popped out Successfully")
            self.count -= 1
            return self.data.pop(0)

    def peek(self):
        return self.data[-1]

    def print_queue(self):
        print("printingnining")
        for i in self.data:
            print(i)
        return


q1 = Queue()
print("Queue full: ", q1.is_Full())
print("Queue empty: ", q1.is_Empty())
q1.enQueue(10)
q1.enQueue(20)
q1.enQueue(30)
q1.enQueue(40)
q1.enQueue(60)
# print(q1.peek())
print(q1.deQueue())
# print(q1.peek())
print(q1.deQueue())
# print(q1.peek())
print(q1.deQueue())
# print(q1.peek())
print(q1.print_queue())
