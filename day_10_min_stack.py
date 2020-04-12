class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        self.stack.append((x, min(self.getMin(), x)))

    def pop(self):
        self.stack = self.stack[:-1]

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return float("inf") if len(self.stack) == 0\
                else self.stack[-1][1]

def main():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())

if __name__ == '__main__':
    main()