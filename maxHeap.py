"""
    Heap sort algorithm
    steps:
        First build Max Heap or Min Heap In order to get sorting
        in ascending and descending order.
        second Delete root with last leaf element
        Third Then again Build Heap.
        fourth Repeat step second and third till single elemnt left in Heap.

"""


def max_heap(arr: list, l: int, i: int):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < l and arr[largest] < arr[left]:
        largest = left
    if right < l and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        max_heap(arr, l, largest)


def swap(arr: list, pos1: int, Pos2: int):
    swap = arr[pos1]
    arr[pos1] = arr[Pos2]
    arr[Pos2] = swap

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    for i in range(int((len(arr)/2))-1, -1, -1):
        max_heap(arr, len(arr), i)
    print(arr)
    for i in range(len(arr)-1, 0, -1):
        swap(arr, 0, i)
        max_heap(arr, i, 0)
    print(arr)