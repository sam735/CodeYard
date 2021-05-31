def init(n:int, m:int):
    t = [[0 for j in range(0,m+1)] for i in range(0,n+1)]
    return t

def get_lcs(t, s1:str, s2:str, n:int, m:int):
    result = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1] == s2[j-1]:
                t[i][j] = 1+ t[i-1][j-1]
                result = max(result,t[i][j])
            else:
                t[i][j] = 0
    return result

if __name__ == "__main__":
    s1 = 'abcde'
    s2 = 'abfce'
    t = init(len(s1),len(s2))
    print(t)
    lcs = get_lcs(t,s1,s2,len(s1), len(s2))
    print(t)
    print(lcs)