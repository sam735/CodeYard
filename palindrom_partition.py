import sys
# recursive approach
# def get_min_partation(s:str, i:int, j:int):
#     if i >= j:
#         return 0
#     min_count = sys.maxsize
#     x = s[i:j+1]
#     if s[i:j+1] == x[::-1]:
#         return 0
    
#     for k in range(i,j):
#         temp_ans = get_min_partation(s,i,k) + get_min_partation(s,k+1,j) + 1
#         if temp_ans < min_count:
#             min_count = temp_ans
#     return min_count

# memoizatied approach
def init(n:int):
    global t
    t = [[-1 for j in range(0,n)] for i in range(0,n)]

def get_min_partation(s:str, i:int, j:int):
    if i >= j:
        return 0
    min_count = sys.maxsize
    x = s[i:j+1]
    if s[i:j+1] == x[::-1]:
        return 0
    if t[i][j] != -1:
        return t[i][j]
    
    for k in range(i,j):
        temp_ans = get_min_partation(s,i,k) + get_min_partation(s,k+1,j) + 1
        if temp_ans < min_count:
            min_count = temp_ans
            t[i][j] = min_count
    return min_count

if __name__ == "__main__":
    s = 'Nitik'
    init(len(s))
    count = get_min_partation(s,0,len(s)-1)
    print(count)