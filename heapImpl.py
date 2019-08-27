from queue import SimpleQueue

def swap(arr,i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def heap_sort(arr:list,i:int,l:int):
    if i > ((l-2)/2):
        return
    largest = i
    if arr[largest] < arr[2*i+1]:
        largest = (2*1)+1
    
    if arr[largest] < arr[2*i+2]:
        largest = (2*1)+2
    
    if i != largest:
        swap(arr,i,largest)
        heap_sort(arr,2*i+1,l)
        heap_sort(arr,2*i+2,l)
        


if __name__ == '__main__':
    arr = [40,60,10,20,50,30]
    l = len(arr)-1
    heap_sort(arr,0,l)
    print(arr)