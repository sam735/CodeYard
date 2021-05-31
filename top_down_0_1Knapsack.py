t = None


def init_matrix(n, m):
    t = [[0 for j in range(0, m+1)] for i in range(0, n+1)]
    return t


def knapsack(items, value, w):
    for i in range(1, len(items)+1):
        for j in range(1, w+1):
            if items[i-1] <= j:
                t[i][j] = max((value[i-1] + t[i-1][j - items[i-1]]), t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[len(items)][w]


if __name__ == "__main__":
    items = [1, 4, 3, 2, 5]
    value = [2, 5, 4, 6, 7]
    w = 5
    t = init_matrix(len(items), w)
    knapsack_value = knapsack(items, value, w)
    print(knapsack_value)
    print(t)