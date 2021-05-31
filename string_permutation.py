def permutaation(s:str,l,r):
    if l == r:
        print(s)
    else:
        for i in range(l,r+1):
            s[l],s[i] = s[i], s[l]
            permutaation(s,l+1,r)
            s[i],s[l] = s[l], s[i]

if __name__ == "__main__ ":
    print('Hi')
    permutaation('ABC',0,2)