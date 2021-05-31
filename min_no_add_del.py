def init(n:int,m:int):
    t = [[0 for j in range(0,m+1)] for i in range(0,n+1)]
    return t

def get_min_add_and_subtract(t, s1:str,s2:str):
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                t[i][j] = t[i-1][j-1] + 1
            else:
                t[i][j] = max(t[i][j-1],t[i-1][j])
    deletion = len(s1) - t[len(s1)][len(s2)]
    addition = len(s2) - t[len(s1)][len(s2)]
    return addition,deletion

if __name__ == '__main__':
    s1 = 'heap'
    s2 = 'hpea'
    t = init(len(s1),len(s2))
    result = get_min_add_and_subtract(t,s1,s2)
    print(result)