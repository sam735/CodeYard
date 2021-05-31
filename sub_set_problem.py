
def sub_problem(arr, n, sum):

    if sum == 0:
        return True

    if n < 0 or sum < 0:
        return False
    
    include = sub_problem(arr, n-1, sum - arr[n-1])

    exclude = sub_problem(arr, n-1, sum)

    return include or exclude


if __name__ == "__main__":
    arr = [2, 3, 7, 8, 10]
    sum = 11
    result = sub_problem(arr, len(arr), sum)
    print(result)
