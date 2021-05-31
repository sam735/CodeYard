
def rotate_matrix_9o(matrix,n):
    for i in range(0,n//2):
        for j in range(i,n-i-1):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][n-i-1]
            matrix[j][n-i-1] = matrix[n-i-1][n-j-1]
            matrix[n-i-1][n-j-1] = matrix[n-j-1][i]
            matrix[n-j-1][i] = tmp

def display(matrix,n):
    for row in matrix:
        print(row)


if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    display(matrix,3)
    rotate_matrix_9o(matrix,3)
    print('After rotation')
    display(matrix,3)
