
def init_t(n, m):
    t = [[-1 for j in range(m+1)] for i in range(n+1)]
    return t


def knapsack(items, weight, capacity, n, t):
    if capacity == 0 or n == 0:
        return 0
    if t[n][capacity] != -1:
        return t[n][capacity]

    if items[n-1] <= capacity:
        t[n][w] = max(weight[n-1] + knapsack(items, weight, capacity-items[n-1], n-1, t),
                                    knapsack(items, weight, capacity-items[n-1], n-1, t))
        return t[n][w]

    elif items[n-1] > capacity:
        t[n][w] = knapsack(items, weight, capacity, n-1, t)
        return t[n][w]


if __name__ == "__main__":
    items = [1, 4, 3, 2, 5]
    weight = [2, 5, 4, 6, 7]
    w = 10
    t = init_t(len(items), w)
    result = knapsack(items, weight, w, len(items), t)
    print(result)