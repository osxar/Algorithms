
"""
Design a stack that supports push, pop, top, and retrieving the maximum element in constant time.

"""

class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxValues = []

    def push(self,value):
        self.stack.append(value)

        if(len(self.maxValues)>0):
            if value>self.maxValues[-1]:
                self.maxValues.append(value)
        else:
            self.maxValues.append(value)

    def pop(self):
        val = self.stack.pop(-1)
        
        if (val == self.maxValues[-1]):
            self.maxValues.pop(-1)

    def top(self):
        return self.stack[-1]

    def getMax(self): 
        return self.maxValues[-1]


obj = MaxStack()

obj.push(7)
obj.push(9)
obj.push(1)
obj.push(5)
obj.pop()

print(obj.getMax())
print(obj.stack)
print(obj.maxValues)
