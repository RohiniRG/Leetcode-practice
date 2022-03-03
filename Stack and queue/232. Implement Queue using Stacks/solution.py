class MyQueue:

    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def push(self, x: int) -> None:
        self.stk1.append(x)
    
    def pop(self) -> int:
        while self.stk1:
            self.stk2.append(self.stk1.pop())
        fr = self.stk2.pop()
        while self.stk2:
            self.stk1.append(self.stk2.pop())
        return fr

    def peek(self) -> int:
        return self.stk1[0]

    def empty(self) -> bool:
        if len(self.stk1) == 0:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
