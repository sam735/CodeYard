from typing import List
from queue import LifoQueue

def get_next_greater_elem(arr:List):
    stack_elm = LifoQueue()
    stack_elm.put(arr[0])
    for i in range(1,len(arr)):
        next = arr[i]
        elem = None
        
        if not stack_elm.empty():
            elem = stack_elm.get()
            while elem < next:
                print('Next greater elemnt of {} is {}'.format(elem,next))
                if stack_elm.empty():
                    break
                elem = stack_elm.get()
            
            if elem > next:
                stack_elm.put(elem)
        
        stack_elm.put(next)
    while not stack_elm.empty():
        elem = stack_elm.get()
        print('Next greater elemnt of {} is -1'.format(elem))
    

if __name__ == '__main__':
    arr = [11, 13, 21, 3]
    get_next_greater_elem(arr)
    

