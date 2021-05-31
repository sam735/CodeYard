import sys
from typing import List


def get_range_set(arr:List,sum:int):
    range_list = []
    t = [[False for j in range(0,sum+1)] for i in range(0,len(arr)+1) ]
    for i in range(0,len(arr)+1):
        t[i][0] = True
    for i in range(1,len(arr)+1):
        for j in range(1,sum+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    for i in range(0,sum+1):
        half = sum/2 if sum%2 == 0 else sum//2+1
        if t[len(arr)][i] == True and i< half:
            range_list.append(i)
    return range_list

def get_min(range_list:List, sum):
    minumum = sys.maxsize
    for item in range_list:
        minumum = min(minumum,sum-2*item)
    return minumum


if __name__ == '__main__':
    arr = [1,7,2]
    range_list = get_range_set(arr,sum(arr))
    min = get_min(range_list,sum(arr))    