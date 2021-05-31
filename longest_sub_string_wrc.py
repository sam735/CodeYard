
def get_longest_substring(arr):
    scan = {}
    start = 0
    max_length = 0
    for i in range(len(arr)):
        if arr[i] in scan:
            start = max(start,scan[arr[i]]+1)
        scan[arr[i]] = i
        max_length = max(max_length,i-start+1)
    return max_length

if __name__ == "__main__":
    s = 'bbbbbswbkp'
    result = get_longest_substring(s)
    print(result)

# def get_max_value(arr,k):
#     sum_val = sum(arr[0:k])
#     max_sum = 0
#     for i in range (k,len(arr)):
#         max_sum = max(sum_val,max_sum)
#         sum_val  = sum_val + arr[i] - arr[i-k]
#     return max(sum_val,max_sum)


# if __name__ == '__main__':
#     arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
#     print(get_max_value(arr,4))
    