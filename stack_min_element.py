from typing import NewType
from collections import  deque

stack = NewType('stack',deque)

def push(stack_obj:stack,elem):
    stack_obj.append(elem)

def pop(stack_obj:stack):
    stack_obj.pop()

def push_min_stack(stack_obj:stack,elem):
    try:
        if stack_obj[-1] > elem:
            stack_obj.append(elem)
        else:
            stack_obj.append(stack_obj[-1])
    except Exception:
        stack_obj.append(elem)
if __name__ == '__main__':
    original_stack = deque()
    min_stack = deque()
    push(original_stack,10)
    push_min_stack(min_stack,10)
    push(original_stack,20)
    push_min_stack(min_stack,20)
    push(original_stack,'5')
    push_min_stack(min_stack,5)
    pop(original_stack)
    pop(min_stack)
    print(original_stack)
    print(min_stack)
