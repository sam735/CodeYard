from typing import List
import sys

t = None
def init_t(n:int):
    global t
    t = [[0 for j in range(0,n+1)] for i in range(0,n+1)]

def get_maxm_sum(arr:List,n:int):
    if n == 3:
        max_sum = arr[0] + arr[2] if arr[0] + arr[2] > arr[1] else arr[1]
        return max_sum
    for i in range(1,n+1):
        count = 0
        for j in range(i+2,n+1):
            if count < 2:
                t[i][j] = t[i][j-2] + arr[i-1] + arr[j-1]
                count += 1
            else:
                t[i][j] = t[i][j-2] + arr[j-1]
    max_sum = -1
    for i in range(1,n+1):
        max_sum = max(max_sum,t[i][n])
    return max_sum



if __name__ == "__main__":
    arr = [5, 5, 10, 100, 10, 5]
    init_t(len(arr))
    print(get_maxm_sum(arr,len(arr)))