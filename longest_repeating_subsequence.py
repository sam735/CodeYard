def init(n:int):
    t = [[0 for j in range(0,n+1)]for i in range(0,n+1)]
    return t

def get_repeating_subsequence(t,s:str):
    for i in range(1,len(s)+1):
        for j in range(1, len(s)+1):
            if s[i-1] == s[j-1] and i != j:
                t[i][j] = t[i-1][j-1] + 1
            else:
                t[i][j] = max(t[i-1][j],t[i][j-1])
    return t[len(s)][len(s)]

if __name__ == '__main__':
    s = 'AABEBCDD'
    t = init(len(s))
    rpsc = get_repeating_subsequence(t,s)
    print(rpsc)