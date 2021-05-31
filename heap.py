def heapify(arr,i,l):
    heighest= i
    left = 2*i + 1
    right = 2*i + 2
    if left < l and arr[heighest] > arr[left]:
        heighest = left
    if right < l and arr[heighest] > arr[right]:
        heighest = right
    if i != heighest:
        arr[i],arr[heighest] = arr[heighest],arr[i]
        heapify(arr,heighest,l)
        
if __name__ == '__main__':
    arr = [10,2,8,16,45,27]
    for i in range(len(arr)//2-1,-1,-1):
        heapify(arr,i,len(arr))
    print(arr)
    for i in range(len(arr)-1,-1,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,0,i)
    print(arr)
