
"""
Design a stack that supports push, pop, top, and retrieving the minimu element in constant time.

"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.minValues = []

    def push(self,value):
        self.stack.append(value)

        if(len(self.minValues)>0):
            if value<self.minValues[-1]:
                self.minValues.append(value)
        else:
            self.minValues.append(value)

    def pop(self):
        val = self.stack.pop(-1)
        
        if (val == self.minValues[-1]):
            self.minValues.pop(-1)

    def top(self):
        return self.stack[-1]

    def getMin(self): 
        return self.minValues[-1]


obj = MinStack()

obj.push(2)
obj.push(4)
obj.push(8)
obj.pop()

print(obj.getMin())
print(obj.stack)
print(obj.minValues)
