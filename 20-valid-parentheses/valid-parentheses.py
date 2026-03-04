class Solution:
    def isValid(self, s: str) -> bool:
        d={"}":"{","]":"[",")":"("}
        stack=Stack_()
        for e in s:
            if e in d.values():
                stack.push(e)
                # print("****")
                # print(stack)
            else:
                if stack.isempty() or stack.peek()!=d[e]:
                    return False
                stack.pop()
        return stack.isempty()

class Stack_:
    def __init__(self):
        self.arr=[]

    def push(self,x):
        return self.arr.append(x)

    def pop(self):
        return self.arr.pop()

    def size(self):
        return len(self.arr)

    def isempty(self):
        return len(self.arr)==0

    def peek(self):
        return self.arr[-1] if self.arr else None