import sys

# Below is the recursive approach
# def get_min_cost(arr,i:int,j:int):
#     min_cost = sys.maxsize
#     if i >= j:
#         return 0
#     for k in range(i,j):
#         temp_cost = get_min_cost(arr,i,k) + get_min_cost(arr,k+1,j) + arr[i-1] * arr[k] * arr[j]
#         if temp_cost < min_cost:
#             min_cost = temp_cost
#     return min_cost

# below is the memoziatied approach
def init(n:int):
    global t
    t = [[-1 for j in range(0,n)]for i in range(0,n)]    

def get_min_cost(arr,i,j):
    if i>=j:
        return 0
    if t[i][j] != -1:
        return t[i][j]
    min_cost = sys.maxsize
    for k in range(i,j):
        temp_cost = get_min_cost(arr,i,k) + get_min_cost(arr,k+1,j) + arr[i-1] * arr[k] * arr[j]
        if temp_cost < min_cost:
            min_cost = temp_cost
            t[i][j] = temp_cost
    return min_cost


if __name__ == "__main__":
    arr = [40,20,30,10,30]
    init(len(arr))
    min_cost = get_min_cost(arr,1,len(arr)-1)
    print(min_cost)