from typing import List

t = None
def init_t(n:int, m:int):
    global t
    t = [[0 for j in range(0,m+1)] for i in range(0,n+1)]

def calculate_lcs(str1:str, str2:str, n:int, m:int):
    for i in range(1,n+1):
        for j in range(1,m+1):
            if str1[i-1] == str2[j-1]:
                t[i][j] = t[i-1][j-1]
            else:
                t[i][j] = 1 + min(t[i-1][j],t[i][j-1],t[i-1][j-1])
    return t[n][m]


if __name__ == '__main__':
    str1 = 'gesek'
    str2 = 'gsseek'
    init_t(len(str1),len(str2))
    print(calculate_lcs(str1,str2,len(str1),len(str2)))
    

