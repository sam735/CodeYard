def partition(arr: list, low,high):
    i = low-1
    pivot = arr[high]
    import pdb; pdb.set_trace()
    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quick_sort(arr: list,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)

if __name__ == "__main__":
    arr = [10,5,18,6,20,3]
    quick_sort(arr,0,len(arr)-1)
    print(arr)
