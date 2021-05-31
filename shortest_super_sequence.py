def init(n:int,m:int):
    t = [[0 for j in range(0,m+1)] for i in range(0,n+1)]
    return t

def get_super_sequnce_length(t, s1:str,s2:str):
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                t[i][j] = t[i-1][j-1] + 1
            else:
                t[i][j] = max(t[i-1][j],t[i][j-1])
    
    return len(s1+s2) - t[len(s1)][len(s2)]

if __name__ == '__main__':
    s1 = 'AGGTAB'
    s2 = 'GXTXAYB'
    t = init(len(s1),len(s2))
    sp = get_super_sequnce_length(t,s1,s2)
    print(sp)