import sys

def check_preorder(arr):
    min = -sys.maxsize - 1
    stack = []
    for item in arr:
        if min > item:
            return False

        while len(stack) > 0 and stack[-1] < item:
            min = stack.pop()
        
        stack.append(item)
    return True

        


if __name__ == "__main__":
    arr = [2, 4, 3]
    print(check_preorder(arr))