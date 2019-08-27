def find_lcs(l1: str, l2: str, length1: int, length2: int):
    """ This functions find the length of each
        common sequence in given string and populate
        matrix[i][j] with that values."""
    """ Theorem:{
                Initialize matrix with 0 for first row and colm
                If s1[i] = s2[j], update matrix[i][j] with value
                of matrix[i-1][j-1]+1
                Else update matrix[i][j] with max of value among
                matrix[i][j-1],matrix[i-1][j]
                Matrix[n][m] will be lcs
                }
     """
    matrix = [[None]*(length1+1) for i in range(0, length2+1)]
    for i in range(0, length2+1):
        for j in range(0, length1+1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif l1[j-1] == l2[i-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])
    lcs = [None for i in range(0, matrix[length2][length1])]
    index = matrix[length2][length1]
    m = length2 
    n = length1
    while(m > -1 and n > -1):
        if l2[m-1] == l1[n-1]:
            lcs[index-1] = l2[m-1]
            index -= 1
            m -= 1
            n -= 1
        elif matrix[m-1][n] > matrix[m][n-1]:
            m -= 1
        else:
            n -= 1
    return lcs


if __name__ == "__main__":
    l1 = input('Enter string1:')
    l2 = input('Enter string2:')
    lcs = find_lcs(l1, l2, len(l1), len(l2))
    print(lcs)
