
## recursion approach
#  
# def get_lcs(s1:str, s2:str, n1:int, n2:int):
#     # print(s1[n1],s2[n2],sep='||')
#     if  n1 == 0 or n2 == 0:
#         return 0
    
#     if s1[n1-1] == s2[n2-1]:
#         return 1 + get_lcs(s1, s2, n1-1, n2-1)
#     else:
#         include_s1 = get_lcs(s1,s2,n1,n2-1)
#         include_s2 = get_lcs(s1,s2,n1-1, n2)
#         return max(include_s1,include_s2)

# Memozation approach
# def init(n:int,m:int):
#     t = [[-1 for j in range(0,m)] for i in range(0,n)]
#     return t
# def get_lcs(t,s1:str, s2:str, n1:int, n2:int):
#     # print(s1[n1],s2[n2],sep='||')
#     if  n1 == 0 or n2 == 0:
#         return 0
    
#     if t[n1-1][n2-1] != -1:
#         return t[n1-1][n2-1]
    
#     elif s1[n1-1] == s2[n2-1]:
#         t[n1-1][n2-1] = 1 + get_lcs(t,s1, s2, n1-1, n2-1)
#         return t[n1-1][n2-1]
#     else:
#         include_s1 = get_lcs(t,s1,s2,n1,n2-1)
#         include_s2 = get_lcs(t,s1,s2,n1-1, n2)
#         t[n1-1][n2-1] = max(include_s1,include_s2)
#         return t[n1-1][n2-1]

# top-down approach
def init(n:int, m:int):
    t = [[0 for j in range(0,m+1)] for i in range(0,n+1)]
    return t


def get_lcs(t, s1:str, s2:str, n:int, m:int):
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1] == s2[j-1]:
                t[i][j] = 1+t[i-1][j-1]
            else:
                t[i][j] = max(t[i][j-1],t[i-1][j])
    return t[n][m]

def print_lcs(t,n:int,m:int,s1:str, s2:str):
    lcs = ''
    i = n
    j = m
    while i > 0:
        while j>0:
            if s1[i-1] == s2[j-1]:
                lcs = lcs + s1[i-1]
                j -= 1
                i -= 1
            else:
                if t[i-1][j] > t[i][j-1]:
                    i -= 1
                else:
                    j -= 1 
    return lcs 

if __name__ == "__main__":
    s1 = 'abdgch'
    s2 = 'abedfhrc'
    t = init(len(s1),len(s2))
    lcs = get_lcs(t,s1,s2,len(s1), len(s2))
    lcs_list = print_lcs(t,len(s1),len(s2),s1,s2)
    print(t)
    print(lcs_list)