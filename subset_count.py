
def init_t(n, m):
    t = [[0 for j in range(0, m+1)] for i in range(0, n+1)]
    for i in range(0, n+1):
        t[i][0] = 1
    return t


def sub_set(arr, sum, n, t):
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][sum]


if __name__ == "__main__":
    arr = [2, 3, 5, 6, 8, 10]
    w = 10
    t = init_t(len(arr), w)
    print(t)
    result = sub_set(arr, w, len(arr), t)
    print(t)
    print(result)