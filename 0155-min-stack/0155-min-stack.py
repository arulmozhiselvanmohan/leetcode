class MinStack:
    
    

    def __init__(self):
        # Main stack to store the values
        self.stack = []
        # Auxiliary stack to store the minimum values
        self.min_stack = []

    def push(self, val: int) -> None:
        # Push the value onto the main stack
        self.stack.append(val)
        # If the min_stack is empty or the current value is smaller than or equal to the current min, push it onto the min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Pop the value from the main stack
        val = self.stack.pop()
        # If the value popped is the same as the current minimum, pop from the min_stack as well
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # Return the top element of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the current minimum value, which is the top of the min_stack
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()