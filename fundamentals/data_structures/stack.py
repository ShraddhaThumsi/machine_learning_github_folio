class Stack:
    def __init__(self,initval=[]):
        self.stack = initval
    def push(self,ele):
        self.stack.append(ele)
        return self.stack
    def pop(self):
        return self.stack.pop(-1)
    def peek(self):
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack)==0
    def check_stack(self):
        print(self.stack)
mystack = Stack([1,2,3])
print(mystack.push(4))
print(mystack.pop())
print(mystack.peek())
print(mystack.is_empty())
print(mystack.check_stack())