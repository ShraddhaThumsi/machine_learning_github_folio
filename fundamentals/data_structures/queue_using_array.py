class Queue:
    def __init__(self,initval=[]):
        self.queue=initval
    def push(self,ele):
        self.queue.append(ele)
        return self.queue
    def pop(self):
        return self.queue.pop(0)
    def peek(self):
        return self.queue[0]
    def check_queue(self):
        return self.queue
    def is_empty(self):
        return len(self.queue) == 0
myqueue=Queue([1,2,3,4])
print(myqueue.check_queue())
print(myqueue.push(5))
print(myqueue.peek())
print(myqueue.pop())
print(myqueue.peek())
print(myqueue.check_queue())
print(myqueue.is_empty())