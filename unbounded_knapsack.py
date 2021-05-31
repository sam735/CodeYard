from typing import List
t = None

def init_dp(m:int,n:int):
    t = [[0 for j in range(0,n+1)]for i in range(0,m+1)]
    return t

def get_max_knapsack_value(t,items:List,value:list,s:int):
    for i in range(1,len(items)+1):
        for j in range(1,s+1):
            if items[i-1] <= j:
                t[i][j] = max((value[i-1]+t[i][j-items[i-1]]),t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[len(items)][s]


if __name__ == "__main__":
    items = [1,4,3,2,5]
    value = [2,5,4,6,7]
    s = 5
    t = init_dp(len(items),s)
    max_value = get_max_knapsack_value(t,items,value,s)
    print(max_value)