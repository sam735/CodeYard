from heapq import heappop, heappush, heapify 


arr = [2, 6, 3, 12, 56, 8] 

def heap_sort():
    heap = arr[:3+1]
    heapify(heap)
    new_arr = []
    for i in range(4,len(arr)):
        new_arr.append(heappop(heap))
        heappush(heap,arr[i])

    while heap:
        new_arr.append(heappop(heap))
    
    return new_arr
if __name__ == "__main__":
   arr = heap_sort()
   print(arr)
