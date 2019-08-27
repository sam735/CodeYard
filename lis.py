
def populate_lis(lis: list, length: int):
    for i in range(0, length):
        lis.append(1)


def find_lis(arr: int, lis: int):
    """
        This function finds the length of "incresing subsequence" at ith
        position and update the value in lis Array which is earlier
        populated by 1.
    """
    """
        Thereom:Iterate over given array and lis array where lis should be
        iterated from '0 To < i' and
        if arry[i]>arr[j] and lis[i] < Lis[j] +1 this means incresing sequence so update 
        lis[i] = lis[j]+1
    """
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    max = 0
    for element in lis:
        if max < element:
            max = element
    return max


if __name__ == "__main__":
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    lis = []
    populate_lis(lis, len(arr))
    max = find_lis(arr, lis)
    print(max)
