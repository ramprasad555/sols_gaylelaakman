def rotate_matrix(mat):
    rm = []
    for _ in range(len(mat)):
        j = -1
        l = []
        for i in range(len(mat)-1,-1,-1):
            j += 1
            l.append(mat[i][j])
        rm.append(l)
    return rm

image = [[2,2,2],[1,1,1],[0,0,0]]
print(image)
print(rotate_matrix(image))
