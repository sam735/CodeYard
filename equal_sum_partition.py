
def init_t(n,m):
    t = [[False for j in range(0,m+1)] for i in range(0,n+1)]
    for i in range(0,n+1):
        t[i][0] = True
    return t


def equal_sum(t, arr, m, n):
    if m % 2 != 0:
        return False
    m = int(m/2) 
    for i in range(1,n+1):
        for j in range(1,m+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    
    return t[n][m]


if __name__ == "__main__":
    arr = [1, 5, 11, 5]
    sum = sum(arr)
    t = init_t(len(arr),sum)
    result = equal_sum(t,arr,sum,len(arr))
    print(result)

