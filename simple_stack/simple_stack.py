stack = []

def push(number):
    stack.append(number)

def pop():
    if stack:
        return stack.pop()
    return None

def peek():
    if stack:
        return stack[-1]
    return None

push(10)
push(3)
print(pop())
print(peek())
