def init(n:int, m:int):
    t = [[0 for j in range(0,m+1)] for i in range(0,n+1)]
    return t


def get_scs(t,s1:str,s2:str):
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                t[i][j] = t[i-1][j-1] + 1
            else:
                t[i][j] = max(t[i-1][j],t[i][j-1])
    i = i-1
    j = j-1
    scs = ''
    while i > 0 and j>0:
        if s1[i] == s2[j]:
            scs = scs + s1[i]
            i -= 1
            j -= 1
        else:
            if t[i-1][j] > t[i][j-1]:
                scs  = scs + s1[i]
                i -= 1
            elif t[i][j-1] >= t[i-1][j]:
                scs = scs + s2[j]
                j -= 1
    while i > 0:
        scs = scs + s1[i-1]
        i -= 1
    while j > 0:
        scs = scs + s2[j-1]
        j -= 1
    return scs

if __name__ == '__main__':
    x = 'abcdaf'
    y = 'acbcf'
    t = init(len(x),len(y))
    print(t)
    scs = get_scs(t,x,y)
    print(t)
    print(scs)

                

