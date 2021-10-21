class Stack():
    def __init__(self, A):
        self.stack = A

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False

    def pop(self):
        if self.isEmpty() == False:
            n = len(self.stack)
            result = self.stack[n-1]
            n -= 1
            self.stack = self.stack[:n]
            return result

    def top(self):
        if self.isEmpty() == False:
            return self.stack[-1]

    def push(self, value):
        self.stack.append(value)


def SortStack(stack):
    if stack.isEmpty() == False:
        less  = Stack([])
        greater = Stack([])
        pivot = stack.pop()
        while stack.isEmpty() == False:
            tmp = stack.pop()
            if tmp <= pivot:
                less.push(tmp)

            else:
                greater.push(tmp)
        SortStack(less)
        SortStack(greater)

        tmpStack = Stack([])

        while less.isEmpty() == False:
            x = less.pop()
            tmpStack.push(x)

        tmpStack.push(pivot)

        while greater.isEmpty() == False:
            x = greater.pop()
            tmpStack.push(x)

        while tmpStack.isEmpty() == False:
            x = tmpStack.pop()
            stack.push(x)

        return stack

if __name__ == "__main__":
    stack = Stack([13, 19, 11, 5, 2, 9, 1])
    result = SortStack(stack)
    print(result.stack)