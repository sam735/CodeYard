
def find_triplet(arr:list):
    arr.sort()
    for i in range(len(arr)-1,2,-1):
        j = i-1
        k = 0
        while(k < j):
            if arr[i] * arr[i] == (arr[j] * arr[j]) + (arr[k] * arr[k]):
                return(arr[i],arr[j],arr[k])
            elif  arr[i] * arr[i] > (arr[j] * arr[j]) + (arr[k] * arr[k]):
                k += 1
            elif  arr[i] * arr[i] < (arr[j] * arr[j]) + (arr[k] * arr[k]):
                j -= 1


if __name__ == "__main__":
    arr = [10, 4, 6, 12, 5]
    triplet = find_triplet(arr)
    print(triplet)