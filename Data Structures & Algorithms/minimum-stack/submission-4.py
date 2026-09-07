class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        if len(self.minStack) > 0:
            if self.minStack[-1] >= val:
                self.minStack.append(val)
        else:
            self.minStack.append(val)

        return self.stack.append(val)
        

    def pop(self) -> None:
        popped = self.stack.pop()
        if len(self.minStack) > 0  and popped == self.minStack[-1]:
            self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if len(self.minStack) > 0:
            return self.minStack[-1]
        else:
            return -1
        
